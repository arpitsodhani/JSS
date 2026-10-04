#!/usr/bin/env python3
"""
AST normalizer that uses language-specific configs to handle Python, Java, JS, C, C++.
"""

import re
import logging
from typing import Dict, List, Set, Tuple
from tools.parser_base import ASTNode
from tools.language_configs import get_language_config


class ASTNormalizer:
    """Normalizes AST for better matching across structures."""
    
    def __init__(self, lang: str):
        self.logger = logging.getLogger("ast_merger.normalizer")
        self.var_counter = 0
        self.renaming_map = {}
        self.config = get_language_config(lang)
    
    def normalize_ast(self, ast: ASTNode, preserve_params: Set[str] = None) -> ASTNode:
        """
        Normalize AST by renaming variables and normalizing expressions.
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
    
    def _is_identifier(self, kind: str) -> bool:
        return kind in self.config["identifier_kinds"]
        
    def _is_literal(self, kind: str) -> bool:
        return kind in self.config["literal_kinds"]
    
    def _collect_variables(self, node: ASTNode, preserve: Set[str]) -> None:
        """Collect variables and create renaming map."""
        if self._is_identifier(node.kind) and node.token:
            # Avoid renaming standard library functions
            if node.token not in preserve and node.token not in self.config["stdlib_funcs"] and node.token not in self.config["keywords"]:
                if node.token not in self.renaming_map:
                    self.renaming_map[node.token] = f"v{self.var_counter}"
                    self.var_counter += 1
        
        # Special logic for Python variable collections on assignments to avoid false matches on properties.
        # But for generic purposes, standardizing identifiers works reasonably universally
        # when not matching stdlib or keywords.
        
        for child in node.children:
            self._collect_variables(child, preserve)
    
    def _apply_renaming(self, node: ASTNode) -> ASTNode:
        """Apply variable renaming to AST."""
        new_token = node.token
        if self._is_identifier(node.kind) and node.token in self.renaming_map:
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
        """Normalize expression patterns like numbers to N."""
        # Normalize integer literals
        if self._is_literal(node.kind):
            normalized_token = "LIT"
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
        """Normalize source text."""
        # Simple generalized comment removal. 
        # Languages vary, but JS/Java/C++ share /* ... */ and //
        # Python uses #, C uses # for preprocessor, so be careful.
        
        # Normalize whitespace
        code = re.sub(r'\s+', ' ', code)
        
        # Normalize simple compound assignments universally
        code = re.sub(r'(\w+)\s*\+=\s*(\w+)', r'\1 = \1 + \2', code)
        code = re.sub(r'(\w+)\s*-=\s*(\w+)', r'\1 = \1 - \2', code)
        code = re.sub(r'(\w+)\s*\*=\s*(\w+)', r'\1 = \1 * \2', code)
        code = re.sub(r'(\w+)\s*/=\s*(\w+)', r'\1 = \1 / \2', code)
        
        return code.strip()
    
    def extract_function_signature(self, code: str) -> str:
        """Extract function signature from code. Fallback to basic regex for C/Java."""
        # Simple regex-based extraction - this works poorly for python 'def name(args):'
        # For now we'll do best effort and rely on parser's signature passing
        match = re.search(r'([\w\s\*]+\s+\w+\s*\([^)]*\))', code)
        if match:
            return match.group(1).strip()
        
        py_match = re.search(r'(def\s+\w+\s*\([^)]*\))', code)
        if py_match:
            return py_match.group(1).strip()
            
        return ""
    
    def get_parameter_names(self, signature: str) -> Set[str]:
        """Extract parameter names from function signature."""
        params = set()
        
        match = re.search(r'\((.*?)\)', signature)
        if match:
            param_list = match.group(1)
            for param in param_list.split(','):
                param = param.strip()
                if param and param != 'void':
                    tokens = re.findall(r'\w+', param)
                    if tokens:
                        params.add(tokens[-1])
        
        return params


def normalize_clause(code: str, lang: str = "c") -> str:
    """Normalize clause code for generic comparison."""
    normalizer = ASTNormalizer(lang)
    return normalizer.normalize_code_text(code)
