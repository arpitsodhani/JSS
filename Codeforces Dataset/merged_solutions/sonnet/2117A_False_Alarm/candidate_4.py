import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        x = numbers[cursor + 1]
        cursor += 2
        cases.append((x, numbers[cursor:cursor + n]))
        cursor += n
    return cases


# --- clause: can_pass :: (x: int, doors: list[int]) -> bool ---
def can_pass(x, doors):
    first = -1
    last = -1
    for i in range(len(doors)):
        if doors[i] == 1:
            if first < 0:
                first = i
            last = i
    if first < 0:
        return True
    return last - first < x


# --- clause: main :: () -> None ---
def main():
    out = []
    for x, doors in read_input():
        out.append("YES" if can_pass(x, doors) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
