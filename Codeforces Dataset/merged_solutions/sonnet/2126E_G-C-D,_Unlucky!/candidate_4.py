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
        prefix = [int(token) for token in data[pos:pos + n]]
        pos += n
        suffix = [int(data[pos + i]) for i in range(n)]
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
    guess = [0] * n
    for i in range(n):
        common = divisor(prefix[i], suffix[i])
        guess[i] = prefix[i] // common * suffix[i]
    running = 0
    for i, value in enumerate(guess):
        running = divisor(running, value)
        if prefix[i] != running:
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
    for case in read_input():
        out.append(feasible(case[0], case[1], case[2]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
