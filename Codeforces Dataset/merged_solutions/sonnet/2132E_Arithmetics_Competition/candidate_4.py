import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int], list[tuple[int, int, int]]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        m = data[pos + 1]
        q = data[pos + 2]
        pos += 3
        a = data[pos:pos + n]
        pos += n
        b = data[pos:pos + m]
        pos += m
        rounds = []
        for _ in range(q):
            rounds.append((data[pos], data[pos + 1], data[pos + 2]))
            pos += 3
        cases.append((a, b, rounds))
    return cases


# --- clause: prefix_sums :: (values: list[int]) -> list[int] ---
def prefix_sums(values):
    order = sorted(values)
    order.reverse()
    sums = [0]
    for value in order:
        sums.append(sums[-1] + value)
    return sums


# --- clause: answer_rounds :: (a: list[int], b: list[int], rounds: list[tuple[int, int, int]]) -> list[int] ---
def answer_rounds(a, b, rounds):
    left = prefix_sums(a)
    right = prefix_sums(b)
    n = len(a)
    m = len(b)
    out = []
    for x, y, z in rounds:
        high = x if x < n else n
        if high > z:
            high = z
        low = z - (y if y < m else m)
        if low < 0:
            low = 0
        if low > high:
            out.append(0)
            continue
        lo = low
        hi = high
        while hi - lo > 2:
            first = lo + (hi - lo) // 3
            second = hi - (hi - lo) // 3
            if left[first] + right[z - first] < left[second] + right[z - second]:
                lo = first + 1
            else:
                hi = second - 1
        best = 0
        for take in range(lo, hi + 1):
            total = left[take] + right[z - take]
            if total > best:
                best = total
        out.append(best)
    return out


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b, rounds in read_input():
        out.extend(map(str, answer_rounds(a, b, rounds)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
