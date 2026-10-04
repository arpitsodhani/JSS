import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int, list[int]]] ---
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


# --- clause: can_land :: (px: int, py: int, qx: int, qy: int, steps: list[int]) -> bool ---
def can_land(px, py, qx, qy, steps):
    gap = (px - qx) * (px - qx) + (py - qy) * (py - qy)
    total = sum(steps)
    longest = max(steps)
    if gap > total * total:
        return False
    slack = 2 * longest - total
    if slack <= 0:
        return True
    return gap >= slack * slack


# --- clause: main :: () -> None ---
def main():
    out = []
    for px, py, qx, qy, steps in read_input():
        out.append("Yes" if can_land(px, py, qx, qy, steps) else "No")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
