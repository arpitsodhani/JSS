import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, str]] ---
def read_input():
    parts = sys.stdin.buffer.read().split()
    idx = 0
    q = int(parts[idx])
    idx += 1
    cases = []
    for _ in range(q):
        n = int(parts[idx])
        start = int(parts[idx + 1])
        seconds = int(parts[idx + 2])
        program = parts[idx + 3].decode()
        idx += 4
        cases.append((n, start, seconds, program))
    return cases


# --- clause: first_zero_time :: (start: int, s: str) -> int ---
def first_zero_time(start, s):
    cur = start
    for i, ch in enumerate(s, start=1):
        cur = cur + 1 if ch == "R" else cur - 1
        if cur == 0:
            return i
    return -1


# --- clause: solve_case :: (n: int, x: int, k: int, s: str) -> int ---
def solve_case(n, x, k, s):
    hit = first_zero_time(x, s)
    if hit == -1 or hit > k:
        return 0
    loop = first_zero_time(0, s)
    if loop == -1:
        return 1
    remaining = k - hit
    return 1 + remaining // loop


# --- clause: main :: () -> None ---
def main():
    lines = []
    for n, start, seconds, program in read_input():
        lines.append(str(solve_case(n, start, seconds, program)))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
