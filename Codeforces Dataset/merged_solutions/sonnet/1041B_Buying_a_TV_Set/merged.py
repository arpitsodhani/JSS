# Clause setup_environment [Confidence: 0.40]
import sys


# Clause solve_logic [Confidence: 0.40]
def main():
    a, b, x, y = map(int, sys.stdin.buffer.read().split())
    d = gcd(x, y)
    x //= d
    y //= d
    ans = min(a // x, b // y)


# Clause finish_program [Confidence: 0.40]
    sys.stdout.write(str(answer) + "\n")

main()


