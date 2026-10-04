#!/usr/bin/env python3
"""
AST parser using libclang for C code analysis.
"""

import hashlib
import logging
from typing import Dict, List, Optional, Set, Tuple, Any
from dataclasses import dataclass
from collections import defaultdict

try:
    import clang.cindex as clang
    LIBCLANG_AVAILABLE = True
except ImportError:
    LIBCLANG_AVAILABLE = False
    logging.warning("libclang not available, parser will fail")


@dataclass
class ASTNode:
    """Simplified AST node representation."""
    kind: str
    token: str
    children: List['ASTNode']
    line: int = 0
    column: int = 0


@dataclass
class ParsedClause:
    """Parsed clause with AST and metadata."""
    clause_id: str
    signature: str
    code: str
    ast: Optional[ASTNode]
    includes: List[str]
    declarations: Dict[str, str]  # name -> type
    error: Optional[str] = None


class LibClangParser:
    """Parser using libclang."""
    
    def __init__(self):
        if not LIBCLANG_AVAILABLE:
            raise ImportError("libclang is not available")
        
        self.index = clang.Index.create()
        self.logger = logging.getLogger("ast_merger.parser")
    
    def parse_clause(self, clause_data: Dict[str, Any], includes: List[str] = None) -> ParsedClause:
        """Parse a single clause."""
        clause_id = clause_data.get("clause_id", "unknown")
        signature = clause_data.get("signature", "")
        code = clause_data.get("code", "")
        
        self.logger.debug(f"Parsing clause {clause_id}")
        
        try:
            # Ensure code has proper function wrapper before parsing
            code_to_parse = self._ensure_function_wrapper(code, signature)
            
            # Prepend includes if provided
            if includes:
                code_to_parse = '\n'.join(includes) + '\n' + code_to_parse
            
            # Parse code
            tu = self.index.parse(
                'temp.c',
                unsaved_files=[('temp.c', code_to_parse)],
                options=clang.TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD
            )
            
            # Check for parse errors
            diagnostics = list(tu.diagnostics)
            # Filter out system header errors (stddef.h, etc.) - treat as warnings
            real_errors = [d for d in diagnostics 
                          if d.severity >= clang.Diagnostic.Error 
                          and "file not found" not in d.spelling.lower()
                          and ".h' file not found" not in d.spelling]
            
            if real_errors:
                error_msgs = [d.spelling for d in real_errors[:3]]
                error_str = "; ".join(error_msgs)
                self.logger.warning(f"Parse errors in clause {clause_id}: {error_str}")
                return ParsedClause(
                    clause_id=clause_id,
                    signature=signature,
                    code=code,  # Store ORIGINAL code
                    ast=None,
                    includes=[],
                    declarations={},
                    error=error_str
                )
            
            # Build AST - extract only the target function, not system headers
            ast = self._build_ast_for_function(tu.cursor, clause_id)
            
            if ast is None:
                # Fallback to full AST if function not found
                ast = self._build_ast(tu.cursor)
            
            # Extract declarations
            declarations = self._extract_declarations(tu.cursor)
            
            return ParsedClause(
                clause_id=clause_id,
                signature=signature,
                code=code,  # Store ORIGINAL code without prepended includes
                ast=ast,
                includes=[],
                declarations=declarations,
                error=None
            )
            
        except Exception as e:
            self.logger.error(f"Failed to parse clause {clause_id}: {e}")
            return ParsedClause(
                clause_id=clause_id,
                signature=signature,
                code=code,
                ast=None,
                includes=[],
                declarations={},
                error=str(e)
            )
    
    def _build_ast_for_function(self, cursor: clang.Cursor, func_name: str) -> Optional[ASTNode]:
        """Build AST for a specific function, skipping system headers."""
        for child in cursor.get_children():
            # Skip system header includes
            if child.location.file and 'include' in str(child.location.file):
                continue
            
            # Find the target function
            if child.kind == clang.CursorKind.FUNCTION_DECL:
                func_id = child.spelling or func_name
                if func_id == func_name or func_name in func_id:
                    return self._build_ast(child)
        
        return None
    
    def _ensure_function_wrapper(self, code: str, signature: str) -> str:
        """Ensure code has proper function wrapper with signature and braces."""
        code = code.strip()
        sig_clean = signature.strip()
        
        # Check if code already has the function wrapper
        if code.startswith(sig_clean):
            # Already has signature
            if '{' in code and code.rstrip().endswith('}'):
                # Has both signature and braces
                return code
            else:
                # Has signature but missing braces - shouldn't happen but handle it
                remaining = code[len(sig_clean):].strip()
                return f"{sig_clean} {{\n{remaining}\n}}"
        
        # Code is just the body without signature/braces
        # Wrap it properly
        return f"{sig_clean} {{\n{code}\n}}"

    
    def _build_ast(self, cursor: clang.Cursor) -> ASTNode:
        """Build simplified AST from libclang cursor."""
        children = []
        for child in cursor.get_children():
            children.append(self._build_ast(child))
        
        token = ""
        if cursor.kind == clang.CursorKind.INTEGER_LITERAL:
            token = "N"  # Normalize integers
        elif cursor.spelling:
            token = cursor.spelling
        
        location = cursor.location
        line = location.line if location.file else 0
        column = location.column if location.file else 0
        
        return ASTNode(
            kind=cursor.kind.name,
            token=token,
            children=children,
            line=line,
            column=column
        )
    
    def _extract_declarations(self, cursor: clang.Cursor) -> Dict[str, str]:
        """Extract variable and function declarations."""
        declarations = {}
        
        def visit(node):
            if node.kind == clang.CursorKind.VAR_DECL:
                declarations[node.spelling] = node.type.spelling
            elif node.kind == clang.CursorKind.PARM_DECL:
                declarations[node.spelling] = node.type.spelling
            elif node.kind == clang.CursorKind.FUNCTION_DECL:
                declarations[node.spelling] = node.type.spelling
            
            for child in node.get_children():
                visit(child)
        
        visit(cursor)
        return declarations
    
    def get_function_body(self, ast: ASTNode) -> Optional[ASTNode]:
        """Extract function body from AST."""
        # Find COMPOUND_STMT which is the function body
        def find_body(node):
            if node.kind == "COMPOUND_STMT":
                return node
            for child in node.children:
                result = find_body(child)
                if result:
                    return result
            return None
        
        return find_body(ast)
    
    def extract_statements(self, body: ASTNode) -> List[ASTNode]:
        """Extract top-level statements from function body."""
        if body.kind != "COMPOUND_STMT":
            return []
        return body.children


def create_parser() -> LibClangParser:
    """Factory function to create parser."""
    if not LIBCLANG_AVAILABLE:
        raise ImportError("libclang is required but not available")
    return LibClangParser()
