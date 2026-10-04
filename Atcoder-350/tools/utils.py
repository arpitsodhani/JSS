#!/usr/bin/env python3
"""
Utility functions for logging, JSON I/O, and common operations.
"""

import json
import logging
import sys
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional


def setup_logging(verbose: bool = False, log_dir: str = "logs") -> logging.Logger:
    """Setup logging configuration."""
    log_path = Path(log_dir)
    log_path.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_path / f"merge_run_{timestamp}.log"
    
    level = logging.DEBUG if verbose else logging.INFO
    
    # Create logger
    logger = logging.getLogger("ast_merger")
    logger.setLevel(level)
    
    # File handler
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    
    # Console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(level)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    logger.addHandler(fh)
    logger.addHandler(ch)
    
    logger.info(f"Logging initialized. Log file: {log_file}")
    return logger


def load_json(filepath: str) -> Dict[str, Any]:
    """Load JSON file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        raise ValueError(f"Failed to load JSON from {filepath}: {e}")


def save_json(data: Dict[str, Any], filepath: str, pretty: bool = True) -> None:
    """Save data to JSON file."""
    try:
        with open(filepath, 'w') as f:
            if pretty:
                json.dump(data, f, indent=2)
            else:
                json.dump(data, f)
    except Exception as e:
        raise ValueError(f"Failed to save JSON to {filepath}: {e}")


def save_text(content: str, filepath: str) -> None:
    """Save text content to file."""
    try:
        with open(filepath, 'w') as f:
            f.write(content)
    except Exception as e:
        raise ValueError(f"Failed to save text to {filepath}: {e}")


def read_text(filepath: str) -> str:
    """Read text content from file."""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except Exception as e:
        raise ValueError(f"Failed to read text from {filepath}: {e}")


def validate_input_schema(data: Dict[str, Any]) -> bool:
    """Validate input JSON schema."""
    required_fields = ["programs"]
    
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")
    
    if not isinstance(data["programs"], list):
        raise ValueError("'programs' must be a list")
    
    if len(data["programs"]) != 5:
        raise ValueError(f"Expected 5 programs, got {len(data['programs'])}")
    
    for i, prog in enumerate(data["programs"]):
        if "id" not in prog:
            raise ValueError(f"Program {i} missing 'id' field")
        if "clauses" not in prog:
            raise ValueError(f"Program {prog['id']} missing 'clauses' field")
        
        for j, clause in enumerate(prog["clauses"]):
            if "clause_id" not in clause:
                raise ValueError(f"Clause {j} in program {prog['id']} missing 'clause_id'")
            if "code" not in clause:
                raise ValueError(f"Clause {clause['clause_id']} missing 'code' field")
    
    return True


def format_error_message(error: Exception, context: str = "") -> str:
    """Format error message with context."""
    msg = f"Error: {str(error)}"
    if context:
        msg = f"{context}: {msg}"
    return msg


def create_report_template() -> Dict[str, Any]:
    """Create empty merge report template."""
    return {
        "merged_program_file": "",
        "timestamp": datetime.now().isoformat(),
        "clauses": {},
        "compile_status": {
            "exit_code": -1,
            "stderr": "",
            "stdout": ""
        },
        "test_results": {
            "passed": 0,
            "total": 0,
            "details": []
        },
        "metrics": {
            "total_fragments": 0,
            "consensus_fragments": 0,
            "average_confidence": 0.0
        },
        "logs": ""
    }


def merge_includes(include_lists: List[List[str]]) -> List[str]:
    """Merge include statements, removing duplicates while preserving order."""
    seen = set()
    merged = []
    
    for includes in include_lists:
        for inc in includes:
            inc_normalized = inc.strip()
            if inc_normalized and inc_normalized not in seen:
                seen.add(inc_normalized)
                merged.append(inc_normalized)
    
    return merged


def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Safe division with default value."""
    if denominator == 0:
        return default
    return numerator / denominator


def truncate_string(s: str, max_length: int = 1000) -> str:
    """Truncate string to maximum length."""
    if len(s) <= max_length:
        return s
    return s[:max_length] + f"... (truncated {len(s) - max_length} chars)"
