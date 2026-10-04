# Clause compare_target_bounds [Confidence: 0.60]
import sys

def solve():
    data = sys.stdin.read().split()
    x = data[0]
    y = data[1]

    pairs = list(zip(x, y))


# Clause detect_impossible_positions [Confidence: 0.20]
    for a, b in pairs:
        if b > a:
            print(-1)
            return


# Clause choose_forced_lower_char [Confidence: 0.20]
    result = []
    for a, b in pairs:
        if b < a:
            result.append(b)


# Clause choose_nonbinding_high_char [Confidence: 0.60]
        else:
            chars[i] = x[i]


# Clause assemble_candidate_string [Confidence: 1.00]
    answer = "".join(chars)


# Clause validate_constructed_output [Confidence: 0.40]
    valid = "".join(min(a, c) for a, c in zip(x, z)) == y
    print(z if valid else -1)

solve()


