import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        target = data[pos + 1]
        pos += 2
        cases.append((target, data[pos:pos + n]))
        pos += n
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
