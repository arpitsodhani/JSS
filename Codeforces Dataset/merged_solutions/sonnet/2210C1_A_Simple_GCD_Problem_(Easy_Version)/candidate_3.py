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
        values = [int(token) for token in data[pos:pos + n]]
        pos += 2 * n
        cases.append(values)
    return cases


# --- clause: divisor :: (x: int, y: int) -> int ---
def divisor(x, y):
    if y == 0:
        return x
    return divisor(y, x % y)


# --- clause: count_moves :: (values: list[int]) -> int ---
def count_moves(values):
    n = len(values)
    total = 0
    for i, value in enumerate(values):
        need = 1
        if i:
            need = divisor(value, values[i - 1])
        if i + 1 < n:
            right = divisor(value, values[i + 1])
            need = need // divisor(need, right) * right
        if need < value:
            total += 1
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for values in read_input():
        out.append(str(count_moves(values)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
