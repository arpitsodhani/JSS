import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    while len(cases) < t:
        n = int(data[pos])
        pos += 1
        prefix = [int(token) for token in data[pos:pos + n]]
        pos += n
        suffix = [int(token) for token in data[pos:pos + n]]
        pos += n
        cases.append((n, prefix, suffix))
    return cases


# --- clause: divisor :: (x: int, y: int) -> int ---
def divisor(x, y):
    while y:
        x, y = y, x % y
    return x


# --- clause: feasible :: (n: int, prefix: list[int], suffix: list[int]) -> str ---
def feasible(n, prefix, suffix):
    guess = []
    for a, b in zip(prefix, suffix):
        guess.append(a // divisor(a, b) * b)
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
    print("\n".join(out))


if __name__ == "__main__":
    main()
