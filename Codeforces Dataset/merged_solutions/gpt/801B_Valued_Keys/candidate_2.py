import sys

def solve():
    x, y = sys.stdin.read().split()[:2]

    # CLAUSE: compare_target_bounds
    n = len(x)
    comparisons = [ord(y[i]) - ord(x[i]) for i in range(n)]

    # CLAUSE: detect_impossible_positions
    if any(delta > 0 for delta in comparisons):
        sys.stdout.write("-1\n")
        return

    # CLAUSE: choose_forced_lower_char
    chars = [""] * n
    for i in range(n):
        if comparisons[i] < 0:
            chars[i] = y[i]

            # CLAUSE: choose_nonbinding_high_char
        else:
            chars[i] = x[i]

    # CLAUSE: assemble_candidate_string
    answer = "".join(chars)

    # CLAUSE: validate_constructed_output
    for i in range(n):
        if min(x[i], answer[i]) != y[i]:
            sys.stdout.write("-1\n")
            return
    sys.stdout.write(answer + "\n")

solve()
