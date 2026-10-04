import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        x = raw[reader + 1]
        reader += 2
        cases.append((x, raw[reader:reader + n]))
        reader += n
    return cases


# --- clause: can_pass :: (x: int, doors: list[int]) -> bool ---
def can_pass(x, doors):
    shut = []
    for i in range(0, len(doors)):
        if doors[i] == 1:
            shut.append(i)
    if not shut:
        return True
    return shut[-1] - shut[0] + 1 <= x


# --- clause: main :: () -> None ---
def main():
    lines = []
    for x, doors in read_input():
        lines.append("YES" if can_pass(x, doors) else "NO")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
