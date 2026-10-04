import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        k = raw[reader + 1]
        reader += 2
        a = raw[reader:reader + n]
        reader += n
        w = raw[reader:reader + k]
        reader += k
        cases.append((a, w))
    return cases


# --- clause: best_happiness :: (a: list[int], w: list[int]) -> int ---
def best_happiness(a, w):
    values = sorted(a, reverse=True)
    sizes = sorted(w)
    k = len(sizes)
    amount = 0
    for i in range(k):
        amount += values[i]
        if sizes[i] == 1:
            amount += values[i]
    tail = len(values) - 1
    for i in range(k - 1, -1, -1):
        if sizes[i] == 1:
            continue
        take = sizes[i] - 1
        amount += values[tail]
        tail -= take
    return amount


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, w in read_input():
        out.append(best_happiness(a, w))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
