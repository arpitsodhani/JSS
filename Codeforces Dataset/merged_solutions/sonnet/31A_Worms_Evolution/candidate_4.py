import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: find_triple :: (a: list[int]) -> tuple[int, int, int] | None ---
def find_triple(a):
    n = len(a)
    sums = {}
    for j in range(n):
        for k in range(j + 1, n):
            sums.setdefault(a[j] + a[k], []).append((j, k))
    for i in range(n):
        for j, k in sums.get(a[i], []):
            if j != i and k != i:
                return i + 1, j + 1, k + 1
    return None


# --- clause: main :: () -> None ---
def main():
    located = find_triple(read_input())
    if located is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("%d %d %d\n" % located)


if __name__ == "__main__":
    main()
