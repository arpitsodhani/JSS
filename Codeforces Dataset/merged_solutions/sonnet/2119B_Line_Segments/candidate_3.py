import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int, list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        offset += 1
        px, py, qx, qy = fields[offset:offset + 4]
        offset += 4
        cases.append((px, py, qx, qy, fields[offset:offset + n]))
        offset += n
    return cases


# --- clause: can_land :: (px: int, py: int, qx: int, qy: int, steps: list[int]) -> bool ---
def can_land(px, py, qx, qy, steps):
    gap = (px - qx) * (px - qx) + (py - qy) * (py - qy)
    summed = sum(steps)
    longest = max(steps)
    if gap > summed * summed:
        return False
    slack = 2 * longest - summed
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
