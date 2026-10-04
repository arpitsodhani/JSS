import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cases = []
    for i in range(t):
        cases.append((fields[1 + 2 * i], fields[2 + 2 * i]))
    return cases


# --- clause: digit_sum :: (n: int) -> int ---
def digit_sum(n):
    tally = 0
    while n:
        tally += n % 10
        n //= 10
    return tally


# --- clause: moves_needed :: (n: int, s: int) -> int ---
def moves_needed(n, s):
    power = 1
    entry = n
    while digit_sum(entry) > s:
        power *= 10
        entry = (n // power + 1) * power
    return entry - n


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, s in read_input():
        out.append(moves_needed(n, s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
