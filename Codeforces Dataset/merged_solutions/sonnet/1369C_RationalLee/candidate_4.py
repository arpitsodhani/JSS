import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        k = numbers[cursor + 1]
        cursor += 2
        a = numbers[cursor:cursor + n]
        cursor += n
        w = numbers[cursor:cursor + k]
        cursor += k
        cases.append((a, w))
    return cases


# --- clause: best_happiness :: (a: list[int], w: list[int]) -> int ---
def best_happiness(a, w):
    values = sorted(a)
    values.reverse()
    sizes = sorted(w)
    k = len(sizes)
    total = 0
    spot = 0
    while spot < k:
        total += values[spot]
        if sizes[spot] == 1:
            total += values[spot]
        spot += 1
    tail = len(values) - 1
    spot = k - 1
    while spot >= 0:
        if sizes[spot] > 1:
            total += values[tail]
            tail -= sizes[spot] - 1
        spot -= 1
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, w in read_input():
        out.append(best_happiness(a, w))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
