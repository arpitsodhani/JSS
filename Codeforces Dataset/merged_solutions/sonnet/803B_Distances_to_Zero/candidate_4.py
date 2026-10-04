import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: zero_distances :: (a: list[int]) -> list[int] ---
def zero_distances(a):
    n = len(a)
    far = n + 1
    dist = [far] * n
    last = -far
    for i in range(n):
        if a[i] == 0:
            last = i
        dist[i] = i - last
    last = 2 * far
    for i in range(n - 1, -1, -1):
        if a[i] == 0:
            last = i
        if last - i < dist[i]:
            dist[i] = last - i
    return dist


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(" ".join(map(str, zero_distances(read_input()))) + "\n")


if __name__ == "__main__":
    main()
