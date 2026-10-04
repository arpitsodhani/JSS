import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


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
    picked = find_triple(read_input())
    if picked is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("%d %d %d\n" % picked)


if __name__ == "__main__":
    main()
