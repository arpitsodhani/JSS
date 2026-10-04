import sys

# CLAUSE: parse_word_count
def parse_word_count(all_words):
    return int(all_words[0])

# CLAUSE: iterate_word_stream
def iterate_word_stream(all_words, n):
    selected_words = all_words[1:]
    for position, word in enumerate(selected_words):
        if position == n:
            break
        word_size = len(word)
        if classify_word_length(word_size):
            yield compose_abbreviation(word, compute_inner_count(word_size))
        else:
            yield preserve_short_word(word)

# CLAUSE: classify_word_length
def classify_word_length(word_size):
    return word_size > 10

# CLAUSE: compute_inner_count
def compute_inner_count(word_size):
    return word_size - 2

# CLAUSE: compose_abbreviation
def compose_abbreviation(word, inner_count):
    return word[0] + "%d" % inner_count + word[-1]

# CLAUSE: preserve_short_word
def preserve_short_word(word):
    return word

# CLAUSE: emit_transformed_sequence
def emit_transformed_sequence(lines):
    sys.stdout.write("\n".join(lines))

tokens = sys.stdin.read().split()
n = parse_word_count(tokens)
emit_transformed_sequence(iterate_word_stream(tokens, n))
