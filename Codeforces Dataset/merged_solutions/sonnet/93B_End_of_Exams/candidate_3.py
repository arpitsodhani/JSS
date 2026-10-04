# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
def emit(parts):
    values = [str(len(parts))]
    for bottle, amount in parts:
        values += [str(bottle), format(amount, ".6f")]
    return " ".join(values)

def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    w = int(tokens[1])
    m = int(tokens[2])
    d = math.gcd(n, m)
    if m > n + n or m // d > 2:
        sys.stdout.write("NO")
        return
    answer = ["YES"]
    portion = n * w / m
    if m <= n:
        start = 0.0
        for _ in range(m):
            end = start + portion
            first = int(start // w) + 1
            last = int((end - 1e-10) // w) + 1
            parts = []
            for bottle in range(first, last + 1):
                left = max(start, (bottle - 1) * w)
                right = min(end, bottle * w)
                parts.append((bottle, right - left))
            answer.append(emit(parts))
            start = end
    else:
        for bottle in range(1, n + 1):
            amount = w * 0.5
            answer.append(emit([(bottle, amount)]))
            answer.append(emit([(bottle, amount)]))
    sys.stdout.write("\n".join(answer))

# CLAUSE: finish_program
main()
