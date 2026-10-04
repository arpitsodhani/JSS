import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    return [(raw[1 + 2 * i], raw[2 + 2 * i]) for i in range(t)]


# --- clause: first_divisible :: (k: int) -> int ---
def first_divisible(k):
    if k == 1:
        return 1
    a = 1
    b = 1
    slot = 2
    while b % k:
        a, b = b, (a + b) % k
        slot += 1
    return slot


# --- clause: main :: () -> None ---
def main():
    mod = 10 ** 9 + 7
    cache = {}
    lines = []
    for n, k in read_input():
        if k not in cache:
            cache[k] = first_divisible(k)
        lines.append(n % mod * (cache[k] % mod) % mod)
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()
