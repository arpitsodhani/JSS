import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: count_triples :: (a: list[int]) -> int ---
def count_triples(a):
    order = sorted(a)
    third = order[2]
    same = 0
    for value in order[:3]:
        if value == third:
            same += 1
    total = 0
    for value in a:
        if value == third:
            total += 1
    if same == 1:
        return total
    if same == 2:
        return total * (total - 1) // 2
    return total * (total - 1) * (total - 2) // 6


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % count_triples(read_input()))


if __name__ == "__main__":
    main()
