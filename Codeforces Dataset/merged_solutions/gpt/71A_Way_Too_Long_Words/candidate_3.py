import sys

# CLAUSE: parse_word_count
def parse_word_count(parts):
    first, rest = parts[0], parts[1:]
    return int(first), rest

# CLAUSE: iterate_word_stream
def iterate_word_stream(words, n):
    transformed = []
    for index in range(n):
        current = words[index]
        current_length = len(current)
        if classify_word_length(current_length):
            inner_count = compute_inner_count(current_length)
            transformed.append(compose_abbreviation(current, inner_count))
        else:
            transformed.append(preserve_short_word(current))
    return transformed

# CLAUSE: classify_word_length
def classify_word_length(word_length):
    return word_length >= 11

# CLAUSE: compute_inner_count
def compute_inner_count(word_length):
    return word_length - 2

# CLAUSE: compose_abbreviation
def compose_abbreviation(word, inner_count):
    pieces = (word[0], str(inner_count), word[-1])
    return "".join(pieces)

# CLAUSE: preserve_short_word
def preserve_short_word(word):
    return word

# CLAUSE: emit_transformed_sequence
def emit_transformed_sequence(items):
    sys.stdout.write("\n".join(items))

tokens = sys.stdin.buffer.read().decode().split()
n, words = parse_word_count(tokens)
output = iterate_word_stream(words, n)
emit_transformed_sequence(output)
