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


# --- clause: best_trap :: (hops: list[int]) -> int ---
def best_trap(hops):
    n = len(hops)
    seen = [0] * (n + 1)
    for value in hops:
        if value <= n:
            seen[value] += 1
    caught = [0] * (n + 1)
    for value in range(1, n + 1):
        if not seen[value]:
            continue
        spot = value
        while spot <= n:
            caught[spot] += seen[value]
            spot += value
    best = 0
    for spot in range(1, n + 1):
        if caught[spot] > best:
            best = caught[spot]
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for hops in read_input():
        out.append(best_trap(hops))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
