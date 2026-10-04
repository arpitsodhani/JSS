import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    at = 1
    cases = []
    for _ in range(t):
        n = tokens[at]
        target = tokens[at + 1]
        at += 2
        cases.append((target, tokens[at:at + n]))
        at += n
    return cases


# --- clause: paint :: (target: int, a: list[int]) -> list[int] ---
def paint(target, a):
    colours = []
    swing = 0
    for value in a:
        if 2 * value < target:
            colours.append(0)
        elif 2 * value > target:
            colours.append(1)
        else:
            colours.append(swing)
            swing = 1 - swing
    return colours


# --- clause: main :: () -> None ---
def main():
    out = []
    for target, a in read_input():
        out.append(" ".join(map(str, paint(target, a))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
