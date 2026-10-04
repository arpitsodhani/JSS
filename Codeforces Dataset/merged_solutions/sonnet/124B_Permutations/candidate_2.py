import sys


# --- clause: read_input :: () -> tuple[int, int, list[str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    numbers = [str(w, "ascii") for w in data[2:2 + n]]
    return n, k, numbers


# --- clause: orderings :: (k: int) -> list[list[int]] ---
def orderings(k):
    result = [[]]
    for _ in range(k):
        grown = []
        for partial in result:
            used = set(partial)
            for slot in range(k):
                if slot in used:
                    continue
                grown.append(partial + [slot])
        result = grown
    return result


# --- clause: smallest_gap :: (n: int, k: int, numbers: list[str], orders: list[list[int]]) -> int ---
def smallest_gap(n, k, numbers, orders):
    best = None
    for order in orders:
        low = None
        high = None
        for text in numbers:
            value = 0
            for slot in order:
                value = value * 10 + (ord(text[slot]) - 48)
            if low is None or value < low:
                low = value
            if high is None or value > high:
                high = value
        gap = high - low
        if best is None or gap < best:
            best = gap
    return best


# --- clause: main :: () -> None ---
def main():
    n, k, numbers = read_input()
    sys.stdout.write("%d\n" % smallest_gap(n, k, numbers, orderings(k)))


if __name__ == "__main__":
    main()
