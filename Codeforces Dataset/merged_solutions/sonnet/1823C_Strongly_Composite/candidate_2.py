import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    at = 1
    cases = []
    for _ in range(t):
        n = tokens[at]
        at += 1
        cases.append(tokens[at:at + n])
        at += n
    return cases


# --- clause: prime_counts :: (a: list[int]) -> dict[int, int] ---
def prime_counts(a):
    tally = {}
    for value in a:
        rest = value
        d = 2
        while d * d <= rest:
            while rest % d == 0:
                tally[d] = tally.get(d, 0) + 1
                rest //= d
            d += 1
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
