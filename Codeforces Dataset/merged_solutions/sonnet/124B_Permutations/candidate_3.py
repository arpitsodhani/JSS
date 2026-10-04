import sys


# --- clause: read_input :: () -> tuple[int, int, list[str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    numbers = [data[2 + i].decode() for i in range(n)]
    return n, k, numbers


# --- clause: orderings :: (k: int) -> list[list[int]] ---
def orderings(k):
    result = [[]]
    for _ in range(k):
        grown = []
        for partial in result:
            for slot in range(k):
                if slot not in partial:
                    grown.append(partial + [slot])
        result = grown
    return result


# --- clause: smallest_gap :: (n: int, k: int, numbers: list[str], orders: list[list[int]]) -> int ---
def smallest_gap(n, k, numbers, orders):
    best = None
    for order in orders:
        made = []
        for text in numbers:
            value = 0
            for slot in order:
                value = value * 10 + int(text[slot])
            made.append(value)
        gap = max(made) - min(made)
        if best is None or gap < best:
            best = gap
    return best


# --- clause: main :: () -> None ---
def main():
    n, k, numbers = read_input()
    print(smallest_gap(n, k, numbers, orderings(k)))


if __name__ == "__main__":
    main()
