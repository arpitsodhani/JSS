# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.60]
def main():
    data = sys.stdin.read().split()
    if not data:
        return

    t = int(data[0])
    pos = 1
    out = []

    for _ in range(t):
        n = int(data[pos])
        k = int(data[pos + 1])
        s = data[pos + 2]
        pos += 3

        left = s.count("0")
        right = s.count("1")
        either = s.count("2")

        ans = []
        for card in range(1, n + 1):
            if card <= left or card > n - right:
                ans.append("-")
            elif card <= left + either or card > n - right - either:
                ans.append("?")
            else:
                ans.append("+")
        out.append("".join(ans))

    sys.stdout.write("\n".join(out))


# Clause finish_program [Confidence: 0.40]
main()


