import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    pos = 1
    for _ in range(t):
        cases.append(tuple(data[pos:pos + 7]))
        pos += 7
    return cases

# Clause can_win [Confidence: 1.00]
def can_win(hc, dc, hm, dm, k, a, w):
    for spent in range(k + 1):
        power = dc + spent * a
        health = hc + (k - spent) * w
        hits = (hm + power - 1) // power
        taken = (health + dm - 1) // dm
        if hits <= taken:
            return True
    return False

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for hc, dc, hm, dm, k, a, w in read_input():
        lines.append("YES" if can_win(hc, dc, hm, dm, k, a, w) else "NO")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

