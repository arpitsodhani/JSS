import sys

def solve():
    x, y = sys.stdin.readline().strip(), sys.stdin.readline().strip()

    # CLAUSE: compare_target_bounds
    indexed = enumerate(zip(x, y))

    # CLAUSE: detect_impossible_positions
    output = []
    impossible = False
    for _, (a, b) in indexed:
        if b > a:
            impossible = True
            break

        # CLAUSE: choose_forced_lower_char
        if b < a:
            output.append(b)

            # CLAUSE: choose_nonbinding_high_char
        else:
            output.append("z")

    if impossible:
        print(-1)
        return

    # CLAUSE: assemble_candidate_string
    z = "".join(output)

    # CLAUSE: validate_constructed_output
    check = [min(a, c) for a, c in zip(x, z)]
    print(z if check == list(y) else -1)

solve()
