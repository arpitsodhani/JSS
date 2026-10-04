import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    return [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(t)]


# --- clause: first_divisible :: (k: int) -> int ---
def first_divisible(k):
    if k == 1:
        return 1
    a = 1
    b = 1
    index = 2
    while b % k:
        a, b = b, (a + b) % k
        index += 1
    return index


# --- clause: main :: () -> None ---
def main():
    mod = 10 ** 9 + 7
    cache = {}
    out = []
    for n, k in read_input():
        if k not in cache:
            cache[k] = first_divisible(k)
        out.append(n % mod * (cache[k] % mod) % mod)
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
