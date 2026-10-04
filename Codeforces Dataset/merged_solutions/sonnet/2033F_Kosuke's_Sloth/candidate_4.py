import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    return [(numbers[1 + 2 * i], numbers[2 + 2 * i]) for i in range(t)]


# --- clause: first_divisible :: (k: int) -> int ---
def first_divisible(k):
    previous = 0
    current = 1
    index = 1
    while True:
        if current % k == 0:
            return index
        previous, current = current, (previous + current) % k
        index += 1


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
