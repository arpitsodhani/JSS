import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: zero_distances :: (a: list[int]) -> list[int] ---
def zero_distances(a):
    n = len(a)
    spots = [i for i in range(n) if a[i] == 0]
    dist = [0] * n
    which = 0
    for i in range(n):
        while which + 1 < len(spots) and abs(spots[which + 1] - i) <= abs(spots[which] - i):
            which += 1
        dist[i] = abs(spots[which] - i)
    return dist


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(" ".join(map(str, zero_distances(read_input()))) + "\n")


if __name__ == "__main__":
    main()
