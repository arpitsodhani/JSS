import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        cases.append(numbers[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: prime_counts :: (a: list[int]) -> dict[int, int] ---
def prime_counts(a):
    tally = {}
    for value in a:
        rest = value
        if rest % 2 == 0:
            while rest % 2 == 0:
                tally[2] = tally.get(2, 0) + 1
                rest //= 2
        d = 3
        while d * d <= rest:
            if rest % d == 0:
                while rest % d == 0:
                    tally[d] = tally.get(d, 0) + 1
                    rest //= d
            d += 2
        if rest > 1:
            tally[rest] = tally.get(rest, 0) + 1
    return tally


# --- clause: most_groups :: (tally: dict[int, int]) -> int ---
def most_groups(tally):
    groups = 0
    spare = 0
    for prime in tally:
        groups += tally[prime] // 2
        spare += tally[prime] % 2
    return groups + spare // 3


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(most_groups(prime_counts(a)))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
