import sys


# --- clause: read_input :: () -> list[tuple[int, str]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    cursor = 1
    cases = []
    for _ in range(t):
        x = int(numbers[cursor + 1])
        s = numbers[cursor + 2].decode()
        cursor += 3
        cases.append((x, s))
    return cases


# --- clause: escape_days :: (x: int, s: str) -> int ---
def escape_days(x, s):
    n = len(s)
    left = s.rfind("#", 0, x - 1) + 1
    spot = s.find("#", x)
    right = n + 1 if spot < 0 else spot + 1
    choices = []
    if x > 1:
        choices.append(min(x, 1 + n + 1 - right))
    if x < n:
        choices.append(min(1 + left, n - x + 1))
    if not choices:
        choices.append(min(1 + left, 1 + n + 1 - right))
    return max(choices)


# --- clause: main :: () -> None ---
def main():
    out = []
    for x, s in read_input():
        out.append(escape_days(x, s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
