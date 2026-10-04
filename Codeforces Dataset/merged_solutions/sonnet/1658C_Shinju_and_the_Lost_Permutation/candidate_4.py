import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        reader += 1
        cases.append(numbers[reader:reader + n])
        reader += n
    return cases


# --- clause: is_possible :: (c: list[int]) -> bool ---
def is_possible(c):
    n = len(c)
    start = -1
    ones = 0
    for i in range(n):
        if c[i] == 1:
            ones += 1
            start = i
    if ones != 1:
        return False
    for step in range(n):
        here = c[(start + step) % n]
        nxt = c[(start + step + 1) % n]
        if nxt - here > 1:
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    out = []
    for c in read_input():
        out.append("YES" if is_possible(c) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
