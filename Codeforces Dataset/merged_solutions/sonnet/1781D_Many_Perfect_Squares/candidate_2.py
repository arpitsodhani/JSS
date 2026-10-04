import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        cases.append(list(map(int, data[pos:pos + n])))
        pos += n
    return cases


# --- clause: square_count :: (values: list[int], shift: int) -> int ---
def square_count(values, shift):
    total = 0
    for value in values:
        target = value + shift
        lo = 0
        hi = 1 << 31
        while lo < hi:
            mid = (lo + hi) // 2
            if mid * mid < target:
                lo = mid + 1
            else:
                hi = mid
        if lo * lo == target:
            total += 1
    return total


# --- clause: best_squareness :: (values: list[int]) -> int ---
def best_squareness(values):
    n = len(values)
    best = 1
    for i in range(n):
        for j in range(i + 1, n):
            gap = values[j] - values[i]
            divisor = 1
            while divisor * divisor <= gap:
                if gap % divisor == 0:
                    other = gap // divisor
                    if (divisor + other) % 2 == 0:
                        low = (other - divisor) // 2
                        shift = low * low - values[i]
                        if shift >= 0:
                            here = square_count(values, shift)
                            if here > best:
                                best = here
                divisor += 1
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for values in read_input():
        out.append(str(best_squareness(values)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
