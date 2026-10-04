"""
Configuration for language-agnostic AST normalizations and filters.
"""

from typing import Dict, Set

# Shared keywords across C-family languages
C_FAMILY_KEYWORDS = {
    'if', 'else', 'while', 'for', 'do', 'switch', 'case', 'default',
    'break', 'continue', 'return', 'goto', 'sizeof', 'typeof'
}

C_FAMILY_OPERATORS = {
    '+', '-', '*', '/', '%', '=', '==', '!=', '<', '>', '<=', '>=',
    '&&', '||', '!', '&', '|', '^', '~', '<<', '>>', 
    '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=', '<<=', '>>=',
    '++', '--', '->', '.', '?', ':'
}

# ----------------- C Configuration -----------------
C_CONFIG = {
    "identifier_kinds": {
        "identifier", "field_identifier", "type_identifier", "primitive_type"
    },
    "literal_kinds": {
        "number_literal", "string_literal", "char_literal"
    },
    "worthy_kinds": {
        "if_statement", "while_statement", "for_statement", "do_statement",
        "return_statement", "compound_statement",
        "call_expression", "binary_expression", "unary_expression",
        "declaration", "assignment_expression", "function_definition"
    },
    "keywords": C_FAMILY_KEYWORDS,
    "operators": C_FAMILY_OPERATORS,
    "stdlib_funcs": {
        'printf', 'scanf', 'malloc', 'free', 'memcpy', 'memset',
        'strlen', 'strcmp', 'strcpy', 'fopen', 'fclose', 'fread', 'fwrite',
        'abs', 'sqrt', 'pow', 'sin', 'cos', 'modf', 'floor', 'ceil'
    }
}

# ----------------- C++ Configuration -----------------
CPP_CONFIG = {
    "identifier_kinds": {
        "identifier", "field_identifier", "type_identifier", "primitive_type", "namespace_identifier"
    },
    "literal_kinds": {
        "number_literal", "string_literal", "char_literal", "boolean_literal", "null"
    },
    "worthy_kinds": {
        "if_statement", "while_statement", "for_statement", "do_statement",
        "return_statement", "compound_statement",
        "call_expression", "binary_expression", "unary_expression",
        "declaration", "assignment_expression", "function_definition",
        "try_statement", "catch_clause", "throw_statement"
    },
    "keywords": C_FAMILY_KEYWORDS | {'try', 'catch', 'throw', 'new', 'delete', 'class', 'struct', 'public', 'private', 'protected'},
    "operators": C_FAMILY_OPERATORS | {'::', '->*'},
    "stdlib_funcs": C_CONFIG["stdlib_funcs"] | {'cout', 'cin', 'endl', 'vector', 'string', 'map', 'set', 'make_unique', 'make_shared'}
}

# ----------------- Python Configuration -----------------
PYTHON_CONFIG = {
    "use_tree_edit_distance": True,
    "ted_timeout_seconds": 600,
    "identifier_kinds": {
        "identifier", "type"
    },
    "literal_kinds": {
        "integer", "float", "string", "true", "false", "none"
    },
    "worthy_kinds": {
        "if_statement", "while_statement", "for_statement",
        "return_statement", "block",
        "call", "binary_operator", "unary_operator", "boolean_operator",
        "assignment", "augmented_assignment", "function_definition",
        "try_statement", "except_clause", "raise_statement"
    },
    "keywords": {
        'if', 'elif', 'else', 'while', 'for', 'in', 'return', 'break', 'continue',
        'pass', 'def', 'class', 'try', 'except', 'finally', 'raise', 'with', 'as',
        'import', 'from', 'global', 'nonlocal', 'assert', 'yield', 'lambda'
    },
    "operators": {
        '+', '-', '*', '/', '//', '%', '**', '=', '==', '!=', '<', '>', '<=', '>=',
        'and', 'or', 'not', 'is', 'in',
        '+=', '-=', '*=', '/=', '//=', '%=', '**=', '&=', '|=', '^=', '<<=', '>>='
    },
    "stdlib_funcs": {
        'print', 'len', 'range', 'enumerate', 'zip', 'map', 'filter', 'sum',
        'min', 'max', 'abs', 'round', 'any', 'all', 'isinstance', 'issubclass',
        'type', 'dir', 'getattr', 'setattr', 'hasattr', 'open'
    }
}

# ----------------- Java Configuration -----------------
JAVA_CONFIG = {
    "identifier_kinds": {
        "identifier", "type_identifier", "scoped_identifier"
    },
    "literal_kinds": {
        "decimal_integer_literal", "hex_integer_literal", "octal_integer_literal",
        "binary_integer_literal", "decimal_floating_point_literal",
        "hex_floating_point_literal", "boolean_literal", "character_literal",
        "string_literal", "null_literal"
    },
    "worthy_kinds": {
        "if_statement", "while_statement", "for_statement", "enhanced_for_statement",
        "do_statement", "return_statement", "block",
        "method_invocation", "binary_expression", "unary_expression",
        "local_variable_declaration", "assignment_expression", "method_declaration",
        "try_statement", "catch_clause", "throw_statement"
    },
    "keywords": C_FAMILY_KEYWORDS | {
        'class', 'interface', 'implements', 'extends', 'public', 'private', 'protected',
        'static', 'final', 'abstract', 'synchronized', 'volatile', 'transient',
        'try', 'catch', 'finally', 'throw', 'throws', 'new', 'instanceof'
    },
    "operators": C_FAMILY_OPERATORS,
    "stdlib_funcs": {
        'System.out.print', 'System.out.println', 'String.valueOf', 'Math.abs',
        'Math.max', 'Math.min', 'Math.sqrt', 'Math.pow', 'equals', 'hashCode', 'toString'
    }
}

# ----------------- JavaScript Configuration -----------------
JS_CONFIG = {
    "identifier_kinds": {
        "identifier", "property_identifier", "shorthand_property_identifier"
    },
    "literal_kinds": {
        "number", "string", "regex", "true", "false", "null", "undefined"
    },
    "worthy_kinds": {
        "if_statement", "while_statement", "for_statement", "for_in_statement",
        "do_statement", "return_statement", "statement_block",
        "call_expression", "binary_expression", "unary_expression",
        "lexical_declaration", "variable_declaration", "assignment_expression", "function_declaration",
        "try_statement", "catch_clause", "throw_statement", "arrow_function"
    },
    "keywords": C_FAMILY_KEYWORDS | {
        'var', 'let', 'const', 'function', 'class', 'extends',
        'try', 'catch', 'finally', 'throw', 'new', 'typeof', 'instanceof',
        'async', 'await', 'yield', 'export', 'import', 'in', 'of'
    },
    "operators": C_FAMILY_OPERATORS | {'===', '!=='},
    "stdlib_funcs": {
        'console.log', 'console.error', 'console.warn',
        'Math.abs', 'Math.max', 'Math.min', 'Math.sqrt', 'Math.pow',
        'parseInt', 'parseFloat', 'isNaN', 'isFinite',
        'Object.keys', 'Object.values', 'Object.entries', 'Array.isArray'
    }
}

# ----------------- Similarity / clustering tuning -----------------
# Calibrated on labelled clause pairs (tools/calibrate_merger_similarity.py in the
# testbed): positives are variants of the same clause, negatives are unrelated
# clauses. The previous settings (set-Jaccard of depth-3 paths, plus free
# size/depth terms, clustered at a hardcoded 0.70) put 30% of unrelated pairs
# above threshold. The blend below reaches recall 0.95 at FPR 0.05.
SIMILARITY_DEFAULTS = {
    # structural features
    "similarity_ngram": 3,            # k-grams over the normalized pre-order node sequence
    "similarity_pattern_depth": 4,    # ancestry-path depth for the weighted path feature
    "similarity_weights": {
        "ngram": 0.30,                # ordering-sensitive
        "kinds": 0.45,                # node-kind multiset overlap
        "paths": 0.20,                # weighted ancestry paths
        "size":  0.05,                # length agreement, deliberately a small term
    },
    # clustering
    "cluster_threshold": 0.60,        # operating point: recall 0.95 / FPR 0.05
    # tree edit distance
    "ted_max_nodes": 500,             # above this, fall back to the fast blend
    "ted_weight": 0.60,               # blend weight of TED against the fast score
    "ted_min_size_ratio": 0.34,       # below this, trees are too different to align
}

_LANG_OVERRIDES = {
    # C-family clauses are typically small function bodies and TED is enabled,
    # so the exact-alignment term carries more of the decision.
    "c":    {"cluster_threshold": 0.62},
    "cpp":  {"cluster_threshold": 0.62},
    "java": {"cluster_threshold": 0.62},
}


def _with_similarity_defaults(config: Dict, lang: str) -> Dict:
    if config.get("_similarity_defaults_applied"):
        return config
    for key, value in SIMILARITY_DEFAULTS.items():
        config.setdefault(key, value)
    for key, value in _LANG_OVERRIDES.get(lang, {}).items():
        config[key] = value
    config["_similarity_defaults_applied"] = True
    return config


def get_language_config(lang: str) -> Dict:
    lang = lang.lower()
    if lang == 'c':
        return _with_similarity_defaults(C_CONFIG, 'c')
    elif lang == 'cpp' or lang == 'c++':
        return _with_similarity_defaults(CPP_CONFIG, 'cpp')
    elif lang == 'python':
        return _with_similarity_defaults(PYTHON_CONFIG, 'python')
    elif lang == 'java':
        return _with_similarity_defaults(JAVA_CONFIG, 'java')
    elif lang in ['javascript', 'js']:
        return _with_similarity_defaults(JS_CONFIG, 'js')
    else:
        # Default to C configuration
        return _with_similarity_defaults(C_CONFIG, 'c')
