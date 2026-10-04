import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    cases = []
    for i in range(t):
        cases.append((raw[1 + 2 * i], raw[2 + 2 * i]))
    return cases


# --- clause: watched_count :: (length: int, k: int) -> int ---
def watched_count(length, k):
    met = 0
    weight = 1
    while length >= k:
        if length % 2:
            met += weight
            length = (length - 1) // 2
        else:
            length //= 2
        weight *= 2
    return met


# --- clause: lucky_value :: (n: int, k: int) -> int ---
def lucky_value(n, k):
    return watched_count(n, k) * (n + 1) // 2


# --- clause: main :: () -> None ---
def main():
    lines = []
    for n, k in read_input():
        lines.append(lucky_value(n, k))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()
