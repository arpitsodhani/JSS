import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: arithmetic_values :: (n: int, a: list[int]) -> list[tuple[int, int]] ---
def arithmetic_values(n, a):
    spots = {}
    for index, value in enumerate(a):
        if value in spots:
            spots[value].append(index)
        else:
            spots[value] = [index]
    found = list()
    for value in sorted(spots.keys()):
        places = spots[value]
        if len(places) == 1:
            found.append((value, 0))
            continue
        gap = places[1] - places[0]
        ok = True
        for i in range(2, len(places)):
            if places[i] - places[i - 1] != gap:
                ok = False
                break
        if ok:
            found.append((value, gap))
    return found

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
