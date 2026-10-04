import sys


# --- clause: read_input :: () -> tuple[list[int], str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    a = [int(raw[1 + i]) for i in range(n)]
    return a, raw[1 + n].decode()


# --- clause: best_value :: (a: list[int], bits: str) -> int ---
def best_value(a, bits):
    n = len(a)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    top = 0
    accumulated = 0
    for level in range(n - 1, -1, -1):
        if bits[level] == "1":
            here = accumulated + prefix[level]
            if here > top:
                top = here
            accumulated += a[level]
    if accumulated > top:
        top = accumulated
    return top


# --- clause: main :: () -> None ---
def main():
    a, bits = read_input()
    sys.stdout.write("%d\n" % best_value(a, bits))


if __name__ == "__main__":
    main()
