import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        target = fields[offset + 1]
        offset += 2
        cases.append((target, fields[offset:offset + n]))
        offset += n
    return cases


# --- clause: paint :: (target: int, a: list[int]) -> list[int] ---
def paint(target, a):
    colours = []
    swing = 0
    for entry in a:
        if 2 * entry < target:
            colours.append(0)
        elif 2 * entry > target:
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
