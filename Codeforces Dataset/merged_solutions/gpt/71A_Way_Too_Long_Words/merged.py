import sys

# CLAUSE: parse_word_count
def parse_word_count(tokens):
    return int(tokens[0]) if tokens else 0

# CLAUSE: iterate_word_stream
def iterate_word_stream(tokens, n):
    results = []
    for word in tokens[1:1 + n]:
        if classify_word_length(word):
            inner = compute_inner_count(word)
            results.append(compose_abbreviation(word, inner))
        else:
            results.append(preserve_short_word(word))
    return results

# CLAUSE: classify_word_length
def classify_word_length(word):
    return len(word) > 10

# CLAUSE: compute_inner_count
def compute_inner_count(word):
    return len(word) - 2

# CLAUSE: compose_abbreviation
def compose_abbreviation(word, inner_count):
    return word[0] + str(inner_count) + word[-1]

# CLAUSE: preserve_short_word
def preserve_short_word(word):
    return word

# CLAUSE: emit_transformed_sequence
def emit_transformed_sequence(results):
    sys.stdout.write("\n".join(results))

data = sys.stdin.read().split()
count = parse_word_count(data)
answers = iterate_word_stream(data, count)
emit_transformed_sequence(answers)
