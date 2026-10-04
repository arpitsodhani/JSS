import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        k = data[pos + 1]
        pos += 2
        a = data[pos:pos + n]
        pos += n
        w = data[pos:pos + k]
        pos += k
        cases.append((a, w))
    return cases


# --- clause: best_happiness :: (a: list[int], w: list[int]) -> int ---
def best_happiness(a, w):
    values = sorted(a, reverse=True)
    sizes = sorted(w)
    k = len(sizes)
    total = 0
    for i in range(k):
        total += values[i]
        if sizes[i] == 1:
            total += values[i]
    tail = len(values) - 1
    for i in range(k - 1, -1, -1):
        if sizes[i] == 1:
            continue
        take = sizes[i] - 1
        total += values[tail]
        tail -= take
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, w in read_input():
        out.append(best_happiness(a, w))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
