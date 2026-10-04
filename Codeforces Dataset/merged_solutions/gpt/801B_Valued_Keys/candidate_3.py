import sys

def choose_char(a, b):
    # CLAUSE: compare_target_bounds
    relation = (b > a) - (b < a)

    # CLAUSE: detect_impossible_positions
    if relation > 0:
        return None

    # CLAUSE: choose_forced_lower_char
    if relation < 0:
        return b

    # CLAUSE: choose_nonbinding_high_char
    return "z"

def solve():
    tokens = sys.stdin.read().split()
    x, y = tokens[0], tokens[1]
    built = []

    for a, b in zip(x, y):
        chosen = choose_char(a, b)
        if chosen is None:
            print(-1)
            return
        built.append(chosen)

    # CLAUSE: assemble_candidate_string
    z = "".join(built)

    # CLAUSE: validate_constructed_output
    valid = "".join(min(a, c) for a, c in zip(x, z)) == y
    print(z if valid else -1)

solve()
