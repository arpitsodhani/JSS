import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: find_triple :: (n: int) -> tuple[int, int, int] | None ---
def find_triple(n):
    if n < 7:
        return None
    rest = n % 3
    if rest == 0:
        base = (1, 4, n - 5)
    elif rest == 1:
        base = (1, 2, n - 3)
    else:
        base = (1, 4, n - 5)
    x, y, z = base
    if z > y and x % 3 and y % 3 and z % 3:
        return x, y, z
    for x in range(1, 10):
        if x % 3 == 0:
            continue
        for y in range(x + 1, 20):
            if y % 3 == 0:
                continue
            z = n - x - y
            if z > y and z % 3:
                return x, y, z
    return None


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n in read_input():
        triple = find_triple(n)
        if triple is None:
            pieces.append("NO")
        else:
            pieces.append("YES")
            pieces.append("%d %d %d" % triple)
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
