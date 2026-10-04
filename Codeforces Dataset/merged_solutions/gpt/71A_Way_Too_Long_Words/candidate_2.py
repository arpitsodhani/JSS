import sys

# CLAUSE: parse_word_count
def parse_word_count():
    line = sys.stdin.readline()
    return int(line.strip())

# CLAUSE: iterate_word_stream
def iterate_word_stream(n):
    for _ in range(n):
        word = sys.stdin.readline().strip()
        if classify_word_length(word):
            middle_size = compute_inner_count(word)
            yield compose_abbreviation(word, middle_size)
        else:
            yield preserve_short_word(word)

# CLAUSE: classify_word_length
def classify_word_length(word):
    word_length = len(word)
    return word_length > 10

# CLAUSE: compute_inner_count
def compute_inner_count(word):
    word_length = len(word)
    return word_length - 2

# CLAUSE: compose_abbreviation
def compose_abbreviation(word, inner_count):
    return f"{word[0]}{inner_count}{word[-1]}"

# CLAUSE: preserve_short_word
def preserve_short_word(word):
    return word

# CLAUSE: emit_transformed_sequence
def emit_transformed_sequence(sequence):
    for item in sequence:
        print(item)

n = parse_word_count()
emit_transformed_sequence(iterate_word_stream(n))
