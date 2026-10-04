import sys

# CLAUSE: parse_word_count
def parse_word_count(raw_tokens):
    return int(raw_tokens.pop(0))

# CLAUSE: iterate_word_stream
def iterate_word_stream(raw_tokens, n):
    output_lines = []
    remaining = n
    while remaining:
        word = raw_tokens.pop(0)
        if classify_word_length(word):
            output_lines.append(compose_abbreviation(word, compute_inner_count(word)))
        else:
            output_lines.append(preserve_short_word(word))
        remaining -= 1
    return output_lines

# CLAUSE: classify_word_length
def classify_word_length(word):
    return not len(word) <= 10

# CLAUSE: compute_inner_count
def compute_inner_count(word):
    return len(word[1:-1])

# CLAUSE: compose_abbreviation
def compose_abbreviation(word, inner_count):
    return "{}{}{}".format(word[0], inner_count, word[-1])

# CLAUSE: preserve_short_word
def preserve_short_word(word):
    return word[:]

# CLAUSE: emit_transformed_sequence
def emit_transformed_sequence(output_lines):
    sys.stdout.write("\n".join(output_lines))

tokens = sys.stdin.read().split()
n = parse_word_count(tokens)
lines = iterate_word_stream(tokens, n)
emit_transformed_sequence(lines)
