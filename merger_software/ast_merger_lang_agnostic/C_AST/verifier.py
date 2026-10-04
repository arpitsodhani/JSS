#!/usr/bin/env python3
"""
Verification and repair harness for compiled programs.
"""

import os
import json
import logging
import subprocess
import tempfile
import time
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from pathlib import Path

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


@dataclass
class CompileResult:
    """Compilation result."""
    success: bool
    exit_code: int
    stdout: str
    stderr: str
    executable_path: Optional[str] = None


@dataclass
class TestResult:
    """Test execution result."""
    test_id: str
    passed: bool
    expected: str
    actual: str
    error: Optional[str] = None


class Verifier:
    """Verifies merged programs through compilation and testing."""
    
    def __init__(self, mode: str = "local"):
        """
        Initialize verifier.
        
        Args:
            mode: Verification mode - 'local', 'docker', or 'judge0'
        """
        self.mode = mode
        self.logger = logging.getLogger("ast_merger.verifier")
        
        if mode == "judge0" and not REQUESTS_AVAILABLE:
            raise ImportError("requests library required for judge0 mode")
    
    def compile(self, code: str, output_file: str = "a.out") -> CompileResult:
        """
        Compile C code.
        
        Args:
            code: C source code
            output_file: Output executable name
        
        Returns:
            Compilation result
        """
        self.logger.info(f"Compiling with mode: {self.mode}")
        
        if self.mode == "local":
            return self._compile_local(code, output_file)
        elif self.mode == "docker":
            return self._compile_docker(code, output_file)
        elif self.mode == "judge0":
            return self._compile_judge0(code)
        else:
            raise ValueError(f"Unknown verification mode: {self.mode}")
    
    def _compile_local(self, code: str, output_file: str) -> CompileResult:
        """Compile using local GCC."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.c', delete=False) as f:
            f.write(code)
            source_file = f.name
        
        try:
            cmd = [
                "gcc",
                "-Wall",
                "-Wextra",
                "-std=c99",
                "-o", output_file,
                source_file
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            success = result.returncode == 0
            
            return CompileResult(
                success=success,
                exit_code=result.returncode,
                stdout=result.stdout,
                stderr=result.stderr,
                executable_path=output_file if success else None
            )
            
        except subprocess.TimeoutExpired:
            return CompileResult(
                success=False,
                exit_code=-1,
                stdout="",
                stderr="Compilation timeout"
            )
        except Exception as e:
            return CompileResult(
                success=False,
                exit_code=-1,
                stdout="",
                stderr=str(e)
            )
        finally:
            if os.path.exists(source_file):
                os.unlink(source_file)
    
    def _compile_docker(self, code: str, output_file: str) -> CompileResult:
        """Compile using Docker sandbox."""
        # Create temporary directory for build
        with tempfile.TemporaryDirectory() as tmpdir:
            source_file = os.path.join(tmpdir, "program.c")
            
            with open(source_file, 'w') as f:
                f.write(code)
            
            try:
                # Run compilation in docker
                cmd = [
                    "docker", "run",
                    "--rm",
                    "-v", f"{tmpdir}:/workspace",
                    "c-sandbox:latest",
                    "gcc",
                    "-Wall",
                    "-Wextra",
                    "-std=c99",
                    "-o", f"/workspace/{output_file}",
                    "/workspace/program.c"
                ]
                
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                
                success = result.returncode == 0
                
                # Copy executable to current directory if successful
                exec_path = None
                if success:
                    src = os.path.join(tmpdir, output_file)
                    dst = output_file
                    if os.path.exists(src):
                        import shutil
                        shutil.copy(src, dst)
                        exec_path = dst
                
                return CompileResult(
                    success=success,
                    exit_code=result.returncode,
                    stdout=result.stdout,
                    stderr=result.stderr,
                    executable_path=exec_path
                )
                
            except subprocess.TimeoutExpired:
                return CompileResult(
                    success=False,
                    exit_code=-1,
                    stdout="",
                    stderr="Docker compilation timeout"
                )
            except Exception as e:
                return CompileResult(
                    success=False,
                    exit_code=-1,
                    stdout="",
                    stderr=f"Docker error: {str(e)}"
                )
    
    def _compile_judge0(self, code: str) -> CompileResult:
        """Compile using Judge0 API."""
        api_key = os.environ.get("JUDGE0_API_KEY", "")
        base_url = os.environ.get("JUDGE0_URL", "https://judge0-ce.p.rapidapi.com")
        
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
        }
        
        payload = {
            "source_code": code,
            "language_id": 50,  # C (GCC 9.2.0)
            "stdin": "",
        }
        
        try:
            # Submit code
            response = requests.post(
                f"{base_url}/submissions",
                json=payload,
                headers=headers,
                params={"base64_encoded": "false", "wait": "true"}
            )
            
            if response.status_code != 201:
                return CompileResult(
                    success=False,
                    exit_code=-1,
                    stdout="",
                    stderr=f"Judge0 submission failed: {response.status_code}"
                )
            
            result_data = response.json()
            
            # Check compilation status
            status_id = result_data.get("status", {}).get("id", 0)
            compile_output = result_data.get("compile_output", "")
            stderr = result_data.get("stderr", "")
            stdout = result_data.get("stdout", "")
            
            success = status_id == 3  # Accepted
            
            return CompileResult(
                success=success,
                exit_code=0 if success else 1,
                stdout=stdout,
                stderr=stderr or compile_output,
                executable_path=None
            )
            
        except Exception as e:
            return CompileResult(
                success=False,
                exit_code=-1,
                stdout="",
                stderr=f"Judge0 error: {str(e)}"
            )
    
    def run_tests(
        self,
        executable: str,
        tests: List[Dict[str, str]]
    ) -> List[TestResult]:
        """
        Run tests on compiled executable.
        
        Args:
            executable: Path to executable
            tests: List of test cases with 'input' and 'expected' keys
        
        Returns:
            List of test results
        """
        results = []
        
        for i, test in enumerate(tests):
            test_id = test.get("id", f"test_{i}")
            input_data = test.get("input", "")
            expected = test.get("expected", "")
            
            try:
                result = subprocess.run(
                    [f"./{executable}"],
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                
                actual = result.stdout.strip()
                passed = actual == expected.strip()
                
                results.append(TestResult(
                    test_id=test_id,
                    passed=passed,
                    expected=expected,
                    actual=actual,
                    error=None if passed else "Output mismatch"
                ))
                
            except subprocess.TimeoutExpired:
                results.append(TestResult(
                    test_id=test_id,
                    passed=False,
                    expected=expected,
                    actual="",
                    error="Timeout"
                ))
            except Exception as e:
                results.append(TestResult(
                    test_id=test_id,
                    passed=False,
                    expected=expected,
                    actual="",
                    error=str(e)
                ))
        
        return results
    
    def analyze_failures(
        self,
        compile_result: CompileResult
    ) -> List[str]:
        """
        Analyze compilation failures and suggest fixes.
        
        Returns:
            List of diagnostic messages
        """
        diagnostics = []
        
        if not compile_result.success:
            stderr = compile_result.stderr
            
            # Common error patterns
            if "undeclared" in stderr or "not declared" in stderr:
                diagnostics.append("Missing variable declarations")
            
            if "implicit declaration" in stderr:
                diagnostics.append("Missing function declarations or includes")
            
            if "conflicting types" in stderr:
                diagnostics.append("Type conflicts in declarations")
            
            if "expected" in stderr:
                diagnostics.append("Syntax errors")
            
            # Add raw stderr for debugging
            diagnostics.append(f"Compiler output: {stderr[:500]}")
        
        return diagnostics
