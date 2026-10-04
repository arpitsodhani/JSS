import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int, int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    reader = 1
    for _ in range(t):
        cases.append(tuple(numbers[reader:reader + 6]))
        reader += 6
    return cases


# --- clause: attacked_from :: (a: int, b: int, x: int, y: int) -> set[tuple[int, int]] ---
def attacked_from(a, b, x, y):
    spots = set()
    for dx, dy in ((a, b), (a, -b), (-a, b), (-a, -b), (b, a), (b, -a), (-b, a), (-b, -a)):
        spots.add((x + dx, y + dy))
    return spots


# --- clause: fork_count :: (a: int, b: int, xk: int, yk: int, xq: int, yq: int) -> int ---
def fork_count(a, b, xk, yk, xq, yq):
    steps = ((a, b), (a, -b), (-a, b), (-a, -b), (b, a), (b, -a), (-b, a), (-b, -a))
    hits = []
    for dx, dy in steps:
        spot = (xk + dx, yk + dy)
        if spot in hits:
            continue
        for ex, ey in steps:
            if xq + ex == spot[0] and yq + ey == spot[1]:
                hits.append(spot)
                break
    return len(hits)


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b, xk, yk, xq, yq in read_input():
        out.append(fork_count(a, b, xk, yk, xq, yq))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
