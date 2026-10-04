import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: arithmetic_values :: (n: int, a: list[int]) -> list[tuple[int, int]] ---
def arithmetic_values(n, a):
    last = {}
    step = {}
    good = {}
    for index, value in enumerate(a):
        if value not in last:
            last[value] = index
            step[value] = 0
            good[value] = True
            continue
        gap = index - last[value]
        if not step[value]:
            step[value] = gap
        elif step[value] != gap:
            good[value] = False
        last[value] = index
    out = []
    for value in sorted(good):
        if good[value]:
            out.append((value, step[value]))
    return out


# --- clause: main :: () -> None ---
def main():
    n, a = read_input()
    found = arithmetic_values(n, a)
    lines = [str(len(found))]
    for value, gap in found:
        lines.append("%d %d" % (value, gap))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
