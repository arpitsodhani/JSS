import sys


# --- clause: read_input :: () -> tuple[int, str, str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return int(numbers[1]), numbers[2].decode(), numbers[3].decode()


# --- clause: count_prefixes :: (k: int, s: str, t: str) -> int ---
def count_prefixes(k, s, t):
    n = len(s)
    width = 1
    total = 0
    level = 0
    while level < n and width < k:
        width *= 2
        if s[level] == "b":
            width -= 1
        if t[level] == "a":
            width -= 1
        if width > k:
            width = k
        total += width
        level += 1
    return total + (n - level) * k


# --- clause: main :: () -> None ---
def main():
    k, s, t = read_input()
    sys.stdout.write("%d\n" % count_prefixes(k, s, t))


if __name__ == "__main__":
    main()
