import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    cases = []
    for i in range(t):
        cases.append((raw[1 + 2 * i], raw[2 + 2 * i]))
    return cases


# --- clause: digit_sum :: (n: int) -> int ---
def digit_sum(n):
    running = 0
    while n:
        running += n % 10
        n //= 10
    return running


# --- clause: moves_needed :: (n: int, s: int) -> int ---
def moves_needed(n, s):
    power = 1
    item = n
    while digit_sum(item) > s:
        power *= 10
        item = (n // power + 1) * power
    return item - n


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, s in read_input():
        out.append(moves_needed(n, s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
