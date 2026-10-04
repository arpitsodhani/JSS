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
    order = sorted(values, reverse=True)
    sums = [0] * (len(order) + 1)
    running = 0
    for i, value in enumerate(order):
        running += value
        sums[i + 1] = running
    return sums


# --- clause: answer_rounds :: (a: list[int], b: list[int], rounds: list[tuple[int, int, int]]) -> list[int] ---
def answer_rounds(a, b, rounds):
    left = prefix_sums(a)
    right = prefix_sums(b)
    n = len(a)
    m = len(b)
    out = []
    for x, y, z in rounds:
        high = min(x, n, z)
        low = z - min(y, m)
        if low < 0:
            low = 0
        if low > high:
            out.append(0)
            continue
        lo = low
        hi = high
        while lo < hi:
            mid = (lo + hi) // 2
            gain = left[mid + 1] - left[mid] - (right[z - mid] - right[z - mid - 1])
            if gain > 0:
                lo = mid + 1
            else:
                hi = mid
        out.append(left[lo] + right[z - lo])
    return out


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b, rounds in read_input():
        out.extend(map(str, answer_rounds(a, b, rounds)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
