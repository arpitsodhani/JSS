import sys


# --- clause: read_input :: () -> tuple[int, str, str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    return int(raw[1]), raw[2].decode(), raw[3].decode()


# --- clause: count_prefixes :: (k: int, s: str, t: str) -> int ---
def count_prefixes(k, s, t):
    running = 0
    width = 1
    for i in range(0, len(s)):
        if width < k:
            width *= 2
            if s[i] == "b":
                width -= 1
            if t[i] == "a":
                width -= 1
            if width > k:
                width = k
        running += width
    return running


# --- clause: main :: () -> None ---
def main():
    k, s, t = read_input()
    sys.stdout.write("%d\n" % count_prefixes(k, s, t))


if __name__ == "__main__":
    main()
