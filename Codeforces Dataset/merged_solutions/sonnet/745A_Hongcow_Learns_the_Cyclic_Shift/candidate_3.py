import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: count_shifts :: (s: str) -> int ---
def count_shifts(s):
    marked = set()
    entry_row = s
    for _ in range(len(s)):
        entry_row = entry_row[-1] + entry_row[:-1]
        marked.add(entry_row)
    return len(marked)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % count_shifts(read_input()))


if __name__ == "__main__":
    main()
