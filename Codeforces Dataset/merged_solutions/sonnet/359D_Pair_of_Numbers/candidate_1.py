import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: reach_left :: (a: list[int]) -> list[int] ---
def reach_left(a):
    n = len(a)
    left = [0] * n
    for i in range(n):
        edge = i
        while edge > 0 and a[edge - 1] % a[i] == 0:
            edge = left[edge - 1]
        left[i] = edge
    return left


# --- clause: reach_right :: (a: list[int]) -> list[int] ---
def reach_right(a):
    n = len(a)
    right = [0] * n
    for i in range(n - 1, -1, -1):
        edge = i
        while edge < n - 1 and a[edge + 1] % a[i] == 0:
            edge = right[edge + 1]
        right[i] = edge
    return right


# --- clause: best_pairs :: (a: list[int], left: list[int], right: list[int]) -> tuple[int, list[int]] ---
def best_pairs(a, left, right):
    span = 0
    for i in range(len(a)):
        if right[i] - left[i] > span:
            span = right[i] - left[i]
    starts = set()
    for i in range(len(a)):
        if right[i] - left[i] == span:
            starts.add(left[i] + 1)
    return span, sorted(starts)


# --- clause: main :: () -> None ---
def main():
    a = read_input()
    left = reach_left(a)
    right = reach_right(a)
    span, starts = best_pairs(a, left, right)
    sys.stdout.write("%d %d\n%s\n" % (len(starts), span, " ".join(map(str, starts))))


if __name__ == "__main__":
    main()
