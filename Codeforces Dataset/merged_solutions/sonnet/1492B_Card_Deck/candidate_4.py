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


# --- clause: best_deck :: (p: list[int]) -> list[int] ---
def best_deck(p):
    n = len(p)
    spot = [0] * (n + 1)
    for i in range(n):
        spot[p[i]] = i
    out = []
    end = n
    value = n
    while end > 0:
        while spot[value] >= end:
            value -= 1
        start = spot[value]
        for i in range(start, end):
            out.append(p[i])
        end = start
    return out


# --- clause: main :: () -> None ---
def main():
    out = []
    for p in read_input():
        out.append(" ".join(map(str, best_deck(p))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
