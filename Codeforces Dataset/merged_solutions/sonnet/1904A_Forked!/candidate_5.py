import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int, int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    cases = []
    offset = 1
    for _ in range(t):
        cases.append(tuple(raw[offset:offset + 6]))
        offset += 6
    return cases


# --- clause: attacked_from :: (a: int, b: int, x: int, y: int) -> set[tuple[int, int]] ---
def attacked_from(a, b, x, y):
    spots = set()
    for dx, dy in ((a, b), (a, -b), (-a, b), (-a, -b), (b, a), (b, -a), (-b, a), (-b, -a)):
        spots.add((x + dx, y + dy))
    return spots


# --- clause: fork_count :: (a: int, b: int, xk: int, yk: int, xq: int, yq: int) -> int ---
def fork_count(a, b, xk, yk, xq, yq):
    return len(attacked_from(a, b, xk, yk) & attacked_from(a, b, xq, yq))


# --- clause: main :: () -> None ---
def main():
    written = []
    for a, b, xk, yk, xq, yq in read_input():
        written.append(fork_count(a, b, xk, yk, xq, yq))
    sys.stdout.write("\n".join(map(str, written)) + "\n")


if __name__ == "__main__":
    main()
