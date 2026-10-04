import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        px, py, qx, qy = numbers[cursor:cursor + 4]
        cursor += 4
        cases.append((px, py, qx, qy, numbers[cursor:cursor + n]))
        cursor += n
    return cases


# --- clause: can_land :: (px: int, py: int, qx: int, qy: int, steps: list[int]) -> bool ---
def can_land(px, py, qx, qy, steps):
    gap = (px - qx) * (px - qx) + (py - qy) * (py - qy)
    reach = 0
    for value in steps:
        if value * value >= gap and reach < value:
            reach = value
    total = 0
    longest = 0
    for value in steps:
        total += value
        if value > longest:
            longest = value
    if gap > total * total:
        return False
    rest = total - longest
    if longest <= rest:
        return True
    return gap >= (longest - rest) * (longest - rest)


# --- clause: main :: () -> None ---
def main():
    out = []
    for px, py, qx, qy, steps in read_input():
        out.append("Yes" if can_land(px, py, qx, qy, steps) else "No")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
