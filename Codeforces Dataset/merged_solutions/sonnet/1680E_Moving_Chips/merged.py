# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 1.00]
def solve_case(n, top, bottom):
    masks = []
    for i in range(n):
        value = 0
        if top[i] == "*":
            value |= 1
        if bottom[i] == "*":
            value |= 2
        masks.append(value)

    left = 0
    while masks[left] == 0:
        left += 1

    right = n - 1
    while masks[right] == 0:
        right -= 1

    first = masks[left]
    dp = [1 if first & 2 else 0, 1 if first & 1 else 0]

    for i in range(left + 1, right + 1):
        mask = masks[i]
        next_dp = [0, 0]
        for row in range(2):
            need = 1 if mask & (2 if row == 0 else 1) else 0
            same = dp[row] + 1 + need
            change = dp[1 - row] + 2 - need
            next_dp[row] = min(same, change)
        dp = next_dp

    return min(dp)

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        top = data[pos + 1]
        bottom = data[pos + 2]
        pos += 3
        out.append(str(solve_case(n, top, bottom)))
    sys.stdout.write("\n".join(out))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


