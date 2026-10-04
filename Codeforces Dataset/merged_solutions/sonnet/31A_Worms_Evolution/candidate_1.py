import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: find_triple :: (a: list[int]) -> tuple[int, int, int] | None ---
def find_triple(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            for k in range(j + 1, n):
                if k == i:
                    continue
                if a[i] == a[j] + a[k]:
                    return i + 1, j + 1, k + 1
    return None


# --- clause: main :: () -> None ---
def main():
    found = find_triple(read_input())
    if found is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("%d %d %d\n" % found)


if __name__ == "__main__":
    main()
