#!/usr/bin/env python3
"""
Fallback parser using tree-sitter for C code.
"""

import logging
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

try:
    from tree_sitter import Language, Parser
    import tree_sitter_c
    TREESITTER_AVAILABLE = True
except ImportError:
    TREESITTER_AVAILABLE = False
    logging.warning("tree-sitter not available")


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
    declarations: Dict[str, str]
    error: Optional[str] = None


class TreeSitterParser:
    """Parser using tree-sitter."""
    
    def __init__(self):
        if not TREESITTER_AVAILABLE:
            raise ImportError("tree-sitter is not available")
        
        self.logger = logging.getLogger("ast_merger.parser")
        
        # Initialize C language
        try:
            C_LANGUAGE = Language(tree_sitter_c.language())
            self.parser = Parser(C_LANGUAGE)
        except Exception as e:
            self.logger.error(f"Failed to initialize tree-sitter: {e}")
            raise
    
    def parse_clause(self, clause_data: Dict[str, Any]) -> ParsedClause:
        """Parse a single clause."""
        clause_id = clause_data.get("clause_id", "unknown")
        signature = clause_data.get("signature", "")
        code = clause_data.get("code", "")
        
        self.logger.debug(f"Parsing clause {clause_id} with tree-sitter")
        
        try:
            tree = self.parser.parse(bytes(code, "utf8"))
            
            if tree.root_node.has_error:
                self.logger.warning(f"Parse errors in clause {clause_id}")
                return ParsedClause(
                    clause_id=clause_id,
                    signature=signature,
                    code=code,
                    ast=None,
                    includes=[],
                    declarations={},
                    error="Parse error detected"
                )
            
            ast = self._build_ast(tree.root_node, code.encode('utf8'))
            declarations = self._extract_declarations(tree.root_node, code.encode('utf8'))
            
            return ParsedClause(
                clause_id=clause_id,
                signature=signature,
                code=code,
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
    
    def _build_ast(self, node, source_code: bytes) -> ASTNode:
        """Build simplified AST from tree-sitter node."""
        children = []
        for child in node.children:
            children.append(self._build_ast(child, source_code))
        
        token = ""
        if node.type == "number_literal":
            token = "N"  # Normalize numbers
        elif node.type == "identifier" or node.type in ["string_literal", "char_literal"]:
            token = source_code[node.start_byte:node.end_byte].decode('utf8')
        
        return ASTNode(
            kind=node.type,
            token=token,
            children=children,
            line=node.start_point[0],
            column=node.start_point[1]
        )
    
    def _extract_declarations(self, node, source_code: bytes) -> Dict[str, str]:
        """Extract variable and function declarations."""
        declarations = {}
        
        def visit(n):
            if n.type == "declaration":
                # Extract variable name and type
                for child in n.children:
                    if child.type == "init_declarator" or child.type == "identifier":
                        name = source_code[child.start_byte:child.end_byte].decode('utf8')
                        # Simplified type extraction
                        declarations[name] = "unknown_type"
            elif n.type == "function_definition":
                for child in n.children:
                    if child.type == "function_declarator":
                        for subchild in child.children:
                            if subchild.type == "identifier":
                                name = source_code[subchild.start_byte:subchild.end_byte].decode('utf8')
                                declarations[name] = "function"
            
            for child in n.children:
                visit(child)
        
        visit(node)
        return declarations


def create_parser() -> TreeSitterParser:
    """Factory function to create tree-sitter parser."""
    if not TREESITTER_AVAILABLE:
        raise ImportError("tree-sitter is required but not available")
    return TreeSitterParser()
