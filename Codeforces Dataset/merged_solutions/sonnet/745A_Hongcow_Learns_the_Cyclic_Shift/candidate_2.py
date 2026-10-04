import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: count_shifts :: (s: str) -> int ---
def count_shifts(s):
    visited = set()
    line = s
    for _ in range(len(s)):
        line = line[-1] + line[:-1]
        visited.add(line)
    return len(visited)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % count_shifts(read_input()))


if __name__ == "__main__":
    main()
