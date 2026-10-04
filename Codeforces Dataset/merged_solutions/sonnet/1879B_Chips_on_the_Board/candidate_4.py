import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        a = numbers[cursor:cursor + n]
        cursor += n
        b = numbers[cursor:cursor + n]
        cursor += n
        cases.append((a, b))
    return cases


# --- clause: cheapest_cover :: (a: list[int], b: list[int]) -> int ---
def cheapest_cover(a, b):
    n = len(a)
    small_a = a[0]
    small_b = b[0]
    total_a = 0
    total_b = 0
    for spot in range(n):
        if a[spot] < small_a:
            small_a = a[spot]
        if b[spot] < small_b:
            small_b = b[spot]
        total_a += a[spot]
        total_b += b[spot]
    return min(small_a * n + total_b, small_b * n + total_a)


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b in read_input():
        out.append(cheapest_cover(a, b))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
