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
        values = list(map(int, data[pos:pos + n]))
        pos += 2 * n
        cases.append(values)
    return cases


# --- clause: divisor :: (x: int, y: int) -> int ---
def divisor(x, y):
    while y != 0:
        x, y = y, x - (x // y) * y
    return x


# --- clause: count_moves :: (values: list[int]) -> int ---
def count_moves(values):
    n = len(values)
    total = 0
    for i in range(n):
        need = 1
        if i > 0:
            left = divisor(values[i], values[i - 1])
            need = left
        if i + 1 < n:
            right = divisor(values[i], values[i + 1])
            need = need * right // divisor(need, right)
        if need != values[i]:
            total += 1
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for values in read_input():
        out.append(str(count_moves(values)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
