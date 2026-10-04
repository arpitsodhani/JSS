import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    return [(fields[1 + 2 * i], fields[2 + 2 * i]) for i in range(t)]


# --- clause: first_divisible :: (k: int) -> int ---
def first_divisible(k):
    if k == 1:
        return 1
    a = 1
    b = 1
    place = 2
    while b % k:
        a, b = b, (a + b) % k
        place += 1
    return place


# --- clause: main :: () -> None ---
def main():
    mod = 10 ** 9 + 7
    cache = {}
    pieces = []
    for n, k in read_input():
        if k not in cache:
            cache[k] = first_divisible(k)
        pieces.append(n % mod * (cache[k] % mod) % mod)
    sys.stdout.write("\n".join(map(str, pieces)) + "\n")


if __name__ == "__main__":
    main()
