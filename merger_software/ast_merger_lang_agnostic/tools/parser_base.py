#!/usr/bin/env python3
"""
Universal parser using tree-sitter for multiple programming languages.
"""

import logging
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

try:
    from tree_sitter import Language, Parser
    TREESITTER_AVAILABLE = True
except ImportError:
    TREESITTER_AVAILABLE = False
    logging.warning("tree-sitter not available")


@dataclass
class ASTNode:
    """Simplified universal AST node representation."""
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


class UniversalParser:
    """Universal parser using tree-sitter for multiple languages."""
    
    def __init__(self, lang_name: str):
        if not TREESITTER_AVAILABLE:
            raise ImportError("tree-sitter is required but not available")
        
        self.logger = logging.getLogger("ast_merger.parser")
        self.lang_name = lang_name.lower()
        
        # Initialize appropriate language
        try:
            if self.lang_name == 'c':
                import tree_sitter_c
                self.ts_lang = Language(tree_sitter_c.language())
            elif self.lang_name in ['cpp', 'c++']:
                import tree_sitter_cpp
                self.ts_lang = Language(tree_sitter_cpp.language())
            elif self.lang_name == 'python':
                import tree_sitter_python
                self.ts_lang = Language(tree_sitter_python.language())
            elif self.lang_name == 'java':
                import tree_sitter_java
                self.ts_lang = Language(tree_sitter_java.language())
            elif self.lang_name in ['javascript', 'js']:
                import tree_sitter_javascript
                self.ts_lang = Language(tree_sitter_javascript.language())
            else:
                self.logger.warning(f"Unsupported language: {self.lang_name}. Defaulting to C.")
                import tree_sitter_c
                self.ts_lang = Language(tree_sitter_c.language())
                
            self.parser = Parser(self.ts_lang)
        except Exception as e:
            self.logger.error(f"Failed to initialize tree-sitter for {self.lang_name}: {e}")
            raise
    
    def parse_clause(self, clause_data: Dict[str, Any]) -> ParsedClause:
        """Parse a single clause."""
        clause_id = clause_data.get("clause_id", "unknown")
        signature = clause_data.get("signature", "")
        code = clause_data.get("code", "")
        
        self.logger.debug(f"Parsing clause {clause_id} with tree-sitter ({self.lang_name})")
        
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
        """Build simplified Universal AST from tree-sitter node."""
        children = []
        for child in node.children:
            children.append(self._build_ast(child, source_code))
        
        token = ""
        # Store exact token for literals and identifiers, or leaf nodes
        if "literal" in node.type or node.type in ["identifier", "type_identifier", "primitive_type", "type", "string"]:
            token = source_code[node.start_byte:node.end_byte].decode('utf8', errors='ignore')
        elif len(children) == 0:
            token = source_code[node.start_byte:node.end_byte].decode('utf8', errors='ignore')
        
        return ASTNode(
            kind=node.type,
            token=token,
            children=children,
            line=node.start_point[0],
            column=node.start_point[1]
        )
    
    def _extract_declarations(self, node, source_code: bytes) -> Dict[str, str]:
        """Extract variable and function declarations (Language agnostic approximation)."""
        declarations = {}
        
        def visit(n):
            # C/C++/Java/JS Variable declarations
            if n.type in ["declaration", "local_variable_declaration", "lexical_declaration", "variable_declaration"]:
                for child in n.children:
                    if child.type in ["init_declarator", "identifier", "variable_declarator"]:
                        name_node = child
                        if child.type != "identifier":
                            for subchild in child.children:
                                if subchild.type == "identifier":
                                    name_node = subchild
                                    break
                        if name_node and name_node.type == "identifier":
                            name = source_code[name_node.start_byte:name_node.end_byte].decode('utf8', errors='ignore')
                            declarations[name] = "variable"
            
            # Python logic (dynamic assignments)
            elif n.type == "assignment":
                for child in n.children:
                    if child.type == "identifier":
                        name = source_code[child.start_byte:child.end_byte].decode('utf8', errors='ignore')
                        declarations[name] = "variable"
                        break
            
            # Function definitions
            elif n.type in ["function_definition", "method_declaration", "function_declaration"]:
                for child in n.children:
                    if child.type in ["function_declarator", "identifier"]:
                        name_node = child
                        if child.type == "function_declarator":
                            for subchild in child.children:
                                if subchild.type == "identifier":
                                    name_node = subchild
                                    break
                        if name_node and name_node.type == "identifier":
                            name = source_code[name_node.start_byte:name_node.end_byte].decode('utf8', errors='ignore')
                            declarations[name] = "function"
            
            for child in n.children:
                visit(child)
        
        visit(node)
        return declarations

def create_parser(lang: str) -> UniversalParser:
    """Factory function to create tree-sitter parser."""
    return UniversalParser(lang)
