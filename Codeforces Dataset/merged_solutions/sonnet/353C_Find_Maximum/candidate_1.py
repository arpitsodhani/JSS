import sys


# --- clause: read_input :: () -> tuple[list[int], str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = [int(data[1 + i]) for i in range(n)]
    return a, data[1 + n].decode()


# --- clause: best_value :: (a: list[int], bits: str) -> int ---
def best_value(a, bits):
    n = len(a)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    best = 0
    running = 0
    for level in range(n - 1, -1, -1):
        if bits[level] == "1":
            here = running + prefix[level]
            if here > best:
                best = here
            running += a[level]
    if running > best:
        best = running
    return best


# --- clause: main :: () -> None ---
def main():
    a, bits = read_input()
    sys.stdout.write("%d\n" % best_value(a, bits))


if __name__ == "__main__":
    main()
