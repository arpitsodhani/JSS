import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    while len(cases) < t:
        n = int(data[pos])
        pos += 1
        cases.append([int(token) for token in data[pos:pos + n]])
        pos += n
    return cases


# --- clause: square_count :: (values: list[int], shift: int) -> int ---
def square_count(values, shift):
    total = 0
    for value in values:
        target = value + shift
        root = int(target ** 0.5)
        while root * root > target:
            root -= 1
        while (root + 1) * (root + 1) <= target:
            root += 1
        if root * root == target:
            total += 1
    return total


# --- clause: best_squareness :: (values: list[int]) -> int ---
def best_squareness(values):
    n = len(values)
    best = 1
    for i in range(n):
        for j in range(i + 1, n):
            gap = values[j] - values[i]
            for divisor in range(1, gap + 1):
                if divisor * divisor > gap:
                    break
                if gap % divisor:
                    continue
                other = gap // divisor
                if (divisor + other) % 2:
                    continue
                low = (other - divisor) // 2
                shift = low * low - values[i]
                if shift < 0:
                    continue
                here = square_count(values, shift)
                if here > best:
                    best = here
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for values in read_input():
        out.append(str(best_squareness(values)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
