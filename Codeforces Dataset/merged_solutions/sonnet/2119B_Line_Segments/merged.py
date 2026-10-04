import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        px, py, qx, qy = data[pos:pos + 4]
        pos += 4
        cases.append((px, py, qx, qy, data[pos:pos + n]))
        pos += n
    return cases

# Clause can_land [Confidence: 1.00]
def can_land(px, py, qx, qy, steps):
    gap = (px - qx) * (px - qx) + (py - qy) * (py - qy)
    amount = sum(steps)
    longest = max(steps)
    if gap > amount * amount:
        return False
    slack = 2 * longest - amount
    if slack <= 0:
        return True
    return gap >= slack * slack

# Clause main [Confidence: 1.00]
def main():
    out = []
    for px, py, qx, qy, steps in read_input():
        out.append("Yes" if can_land(px, py, qx, qy, steps) else "No")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

