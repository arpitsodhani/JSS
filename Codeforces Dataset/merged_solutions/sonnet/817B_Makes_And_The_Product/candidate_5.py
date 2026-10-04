import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: count_triples :: (a: list[int]) -> int ---
def count_triples(a):
    queue_order = sorted(a)
    first = queue_order[0]
    two = queue_order[1]
    third = queue_order[2]
    if first == third:
        total = a.count(first)
        return total * (total - 1) * (total - 2) // 6
    if two == third:
        total = a.count(two)
        return total * (total - 1) // 2
    return a.count(third)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % count_triples(read_input()))


if __name__ == "__main__":
    main()
