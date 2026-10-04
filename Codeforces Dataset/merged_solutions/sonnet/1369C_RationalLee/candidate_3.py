import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        k = fields[offset + 1]
        offset += 2
        a = fields[offset:offset + n]
        offset += n
        w = fields[offset:offset + k]
        offset += k
        cases.append((a, w))
    return cases


# --- clause: best_happiness :: (a: list[int], w: list[int]) -> int ---
def best_happiness(a, w):
    values = sorted(a, reverse=True)
    sizes = sorted(w)
    k = len(sizes)
    summed = 0
    for i in range(k):
        summed += values[i]
        if sizes[i] == 1:
            summed += values[i]
    tail = len(values) - 1
    for i in range(k - 1, -1, -1):
        if sizes[i] == 1:
            continue
        take = sizes[i] - 1
        summed += values[tail]
        tail -= take
    return summed


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, w in read_input():
        out.append(best_happiness(a, w))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
