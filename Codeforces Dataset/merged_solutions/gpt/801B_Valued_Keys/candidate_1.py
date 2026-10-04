import sys

def solve():
    data = sys.stdin.read().split()
    x = data[0]
    y = data[1]

    # CLAUSE: compare_target_bounds
    pairs = list(zip(x, y))

    # CLAUSE: detect_impossible_positions
    for a, b in pairs:
        if b > a:
            print(-1)
            return

    # CLAUSE: choose_forced_lower_char
    result = []
    for a, b in pairs:
        if b < a:
            result.append(b)

            # CLAUSE: choose_nonbinding_high_char
        else:
            result.append("z")

    # CLAUSE: assemble_candidate_string
    z = "".join(result)

    # CLAUSE: validate_constructed_output
    if all(min(a, c) == b for a, b, c in zip(x, y, z)):
        print(z)
    else:
        print(-1)

if __name__ == "__main__":
    solve()
