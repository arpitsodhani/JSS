import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


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
    hit = find_triple(read_input())
    if hit is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("%d %d %d\n" % hit)


if __name__ == "__main__":
    main()
