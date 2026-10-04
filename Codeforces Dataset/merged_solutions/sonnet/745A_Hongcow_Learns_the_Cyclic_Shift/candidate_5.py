import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: count_shifts :: (s: str) -> int ---
def count_shifts(s):
    met = set()
    band = s
    for _ in range(0, len(s)):
        band = band[-1] + band[:-1]
        met.add(band)
    return len(met)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % count_shifts(read_input()))


if __name__ == "__main__":
    main()
