import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        prefix = list(map(int, data[pos:pos + n]))
        pos += n
        suffix = [int(token) for token in data[pos:pos + n]]
        pos += n
        cases.append((n, prefix, suffix))
    return cases


# --- clause: divisor :: (x: int, y: int) -> int ---
def divisor(x, y):
    while y != 0:
        x, y = y, x - y * (x // y)
    return x


# --- clause: feasible :: (n: int, prefix: list[int], suffix: list[int]) -> str ---
def feasible(n, prefix, suffix):
    guess = [0] * n
    for i in range(n):
        common = divisor(prefix[i], suffix[i])
        guess[i] = prefix[i] // common * suffix[i]
    running = 0
    for i in range(n):
        running = divisor(running, guess[i])
        if running != prefix[i]:
            return "NO"
    running = 0
    for i in range(n - 1, -1, -1):
        running = divisor(running, guess[i])
        if running != suffix[i]:
            return "NO"
    return "YES"


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, prefix, suffix in read_input():
        out.append(feasible(n, prefix, suffix))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
