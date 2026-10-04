#!/usr/bin/env python3
"""
AST normalization and canonicalization utilities.
"""

import re
import logging
from typing import Dict, List, Set, Tuple
from tools.parser_libclang import ASTNode


class ASTNormalizer:
    """Normalizes AST for better matching."""
    
    def __init__(self):
        self.logger = logging.getLogger("ast_merger.normalizer")
        self.var_counter = 0
        self.renaming_map = {}
    
    def normalize_ast(self, ast: ASTNode, preserve_params: Set[str] = None) -> ASTNode:
        """
        Normalize AST by renaming variables and normalizing expressions.
        
        Args:
            ast: Input AST node
            preserve_params: Set of parameter names to preserve
        
        Returns:
            Normalized AST node
        """
        if preserve_params is None:
            preserve_params = set()
        
        self.var_counter = 0
        self.renaming_map = {}
        
        # First pass: identify variables to rename
        self._collect_variables(ast, preserve_params)
        
        # Second pass: apply renaming
        normalized = self._apply_renaming(ast)
        
        # Third pass: normalize expressions
        normalized = self._normalize_expressions(normalized)
        
        return normalized
    
    def _collect_variables(self, node: ASTNode, preserve: Set[str]) -> None:
        """Collect variables and create renaming map."""
        if node.kind in ["VAR_DECL", "DECL_REF_EXPR"] and node.token:
            if node.token not in preserve and node.token not in self.renaming_map:
                self.renaming_map[node.token] = f"v{self.var_counter}"
                self.var_counter += 1
        
        for child in node.children:
            self._collect_variables(child, preserve)
    
    def _apply_renaming(self, node: ASTNode) -> ASTNode:
        """Apply variable renaming to AST."""
        new_token = node.token
        if node.kind in ["VAR_DECL", "DECL_REF_EXPR", "identifier"] and node.token in self.renaming_map:
            new_token = self.renaming_map[node.token]
        
        new_children = [self._apply_renaming(child) for child in node.children]
        
        return ASTNode(
            kind=node.kind,
            token=new_token,
            children=new_children,
            line=node.line,
            column=node.column
        )
    
    def _normalize_expressions(self, node: ASTNode) -> ASTNode:
        """Normalize expression patterns."""
        # Normalize compound assignments: x += y -> x = x + y
        if node.kind == "COMPOUND_ASSIGN_OPERATOR":
            # This is simplified; real implementation would reconstruct the expression
            pass
        
        # Normalize integer literals
        if node.kind in ["INTEGER_LITERAL", "number_literal"]:
            normalized_token = "N"
        else:
            normalized_token = node.token
        
        new_children = [self._normalize_expressions(child) for child in node.children]
        
        return ASTNode(
            kind=node.kind,
            token=normalized_token,
            children=new_children,
            line=node.line,
            column=node.column
        )
    
    def normalize_code_text(self, code: str) -> str:
        """Normalize C code text."""
        # Remove comments
        code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
        code = re.sub(r'//.*?$', '', code, flags=re.MULTILINE)
        
        # Normalize whitespace
        code = re.sub(r'\s+', ' ', code)
        
        # Normalize compound assignments
        code = re.sub(r'(\w+)\s*\+=\s*(\w+)', r'\1 = \1 + \2', code)
        code = re.sub(r'(\w+)\s*-=\s*(\w+)', r'\1 = \1 - \2', code)
        code = re.sub(r'(\w+)\s*\*=\s*(\w+)', r'\1 = \1 * \2', code)
        code = re.sub(r'(\w+)\s*/=\s*(\w+)', r'\1 = \1 / \2', code)
        
        return code.strip()
    
    def extract_function_signature(self, code: str) -> str:
        """Extract function signature from code."""
        # Simple regex-based extraction
        match = re.search(r'([\w\s\*]+\s+\w+\s*\([^)]*\))', code)
        if match:
            return match.group(1).strip()
        return ""
    
    def get_parameter_names(self, signature: str) -> Set[str]:
        """Extract parameter names from function signature."""
        params = set()
        
        # Extract parameters from signature
        match = re.search(r'\((.*?)\)', signature)
        if match:
            param_list = match.group(1)
            # Split by comma and extract variable names
            for param in param_list.split(','):
                param = param.strip()
                if param and param != 'void':
                    # Extract last identifier (variable name)
                    tokens = re.findall(r'\w+', param)
                    if tokens:
                        params.add(tokens[-1])
        
        return params


def normalize_clause(code: str) -> str:
    """Normalize clause code for better comparison."""
    normalizer = ASTNormalizer()
    return normalizer.normalize_code_text(code)
