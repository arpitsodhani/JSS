import sys


# --- clause: read_input :: () -> tuple[list[int], str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    n = int(numbers[0])
    a = [int(numbers[1 + i]) for i in range(n)]
    return a, numbers[1 + n].decode()


# --- clause: best_value :: (a: list[int], bits: str) -> int ---
def best_value(a, bits):
    n = len(a)
    suffix = 0
    best = 0
    running = 0
    level = n - 1
    prefix = []
    total = 0
    for value in a:
        prefix.append(total)
        total += value
    while level >= 0:
        if bits[level] == "1":
            candidate = running + prefix[level]
            if candidate > best:
                best = candidate
            running += a[level]
        level -= 1
    return running if running > best else best


# --- clause: main :: () -> None ---
def main():
    a, bits = read_input()
    sys.stdout.write("%d\n" % best_value(a, bits))


if __name__ == "__main__":
    main()
