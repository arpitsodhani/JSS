import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cases = []
    for i in range(t):
        cases.append((fields[1 + 2 * i], fields[2 + 2 * i]))
    return cases


# --- clause: watched_count :: (length: int, k: int) -> int ---
def watched_count(length, k):
    marked = 0
    weight = 1
    while length >= k:
        if length % 2:
            marked += weight
            length = (length - 1) // 2
        else:
            length //= 2
        weight *= 2
    return marked


# --- clause: lucky_value :: (n: int, k: int) -> int ---
def lucky_value(n, k):
    return watched_count(n, k) * (n + 1) // 2


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n, k in read_input():
        pieces.append(lucky_value(n, k))
    sys.stdout.write("\n".join(map(str, pieces)) + "\n")


if __name__ == "__main__":
    main()
