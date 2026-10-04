import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    at = 1
    cases = []
    for _ in range(t):
        n = tokens[at]
        x = tokens[at + 1]
        at += 2
        cases.append((x, tokens[at:at + n]))
        at += n
    return cases


# --- clause: can_pass :: (x: int, doors: list[int]) -> bool ---
def can_pass(x, doors):
    shut = []
    for i in range(len(doors)):
        if doors[i] == 1:
            shut.append(i)
    if not shut:
        return True
    return shut[-1] - shut[0] + 1 <= x


# --- clause: main :: () -> None ---
def main():
    out = []
    for x, doors in read_input():
        out.append("YES" if can_pass(x, doors) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
