import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int, int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    pos = 1
    for _ in range(t):
        cases.append(tuple(data[pos:pos + 6]))
        pos += 6
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
    out = []
    for a, b, xk, yk, xq, yq in read_input():
        out.append(fork_count(a, b, xk, yk, xq, yq))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
