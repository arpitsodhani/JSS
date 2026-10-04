import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: count_shifts :: (s: str) -> int ---
def count_shifts(s):
    seen = set()
    row = s
    for _ in range(len(s)):
        row = row[-1] + row[:-1]
        seen.add(row)
    return len(seen)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % count_shifts(read_input()))


if __name__ == "__main__":
    main()
