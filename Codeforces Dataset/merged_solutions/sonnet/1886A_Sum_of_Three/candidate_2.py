import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: find_triple :: (n: int) -> tuple[int, int, int] | None ---
def find_triple(n):
    for x in range(1, 12):
        if x % 3 == 0:
            continue
        for y in range(x + 1, 24):
            if y % 3 == 0:
                continue
            z = n - x - y
            if z > y and z % 3:
                return x, y, z
    return None


# --- clause: main :: () -> None ---
def main():
    lines = []
    for n in read_input():
        triple = find_triple(n)
        if triple is None:
            lines.append("NO")
        else:
            lines.append("YES")
            lines.append("%d %d %d" % triple)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
