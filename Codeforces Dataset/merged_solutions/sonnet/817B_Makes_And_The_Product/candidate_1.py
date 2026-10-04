import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: count_triples :: (a: list[int]) -> int ---
def count_triples(a):
    order = sorted(a)
    first = order[0]
    second = order[1]
    third = order[2]
    if first == third:
        total = a.count(first)
        return total * (total - 1) * (total - 2) // 6
    if second == third:
        total = a.count(second)
        return total * (total - 1) // 2
    return a.count(third)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % count_triples(read_input()))


if __name__ == "__main__":
    main()
