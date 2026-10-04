import sys


# --- clause: read_input :: () -> tuple[list[int], str] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    n = int(fields[0])
    a = [int(fields[1 + i]) for i in range(n)]
    return a, fields[1 + n].decode()


# --- clause: best_value :: (a: list[int], bits: str) -> int ---
def best_value(a, bits):
    n = len(a)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    finest = 0
    rolling = 0
    for level in range(n - 1, -1, -1):
        if bits[level] == "1":
            here = rolling + prefix[level]
            if here > finest:
                finest = here
            rolling += a[level]
    if rolling > finest:
        finest = rolling
    return finest


# --- clause: main :: () -> None ---
def main():
    a, bits = read_input()
    sys.stdout.write("%d\n" % best_value(a, bits))


if __name__ == "__main__":
    main()
