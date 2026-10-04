import sys

def solve():
    data = sys.stdin.buffer.read().split()
    x = data[0].decode()
    y = data[1].decode()

    # CLAUSE: compare_target_bounds
    compared = tuple((a, b, a == b, b < a, b > a) for a, b in zip(x, y))

    # CLAUSE: detect_impossible_positions
    if next((True for _, _, _, _, bad in compared if bad), False):
        print(-1)
        return

    # CLAUSE: choose_forced_lower_char
    def forced_or_empty(item):
        a, b, equal, lower, bad = item
        if lower:
            return b

        # CLAUSE: choose_nonbinding_high_char
        if equal:
            return "z"
        return ""

    parts = [forced_or_empty(item) for item in compared]

    # CLAUSE: assemble_candidate_string
    z = "".join(parts)

    # CLAUSE: validate_constructed_output
    print(z if len(z) == len(x) and all(min(a, c) == b for a, b, c in zip(x, y, z)) else -1)

solve()
