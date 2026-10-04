import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: split_message :: (t: str) -> str | None ---
def split_message(t):
    n = len(t)
    for width in range(n // 2 + 1, n):
        if 2 * width - n <= 0:
            continue
        if t[:width] == t[n - width:]:
            return t[:width]
    return None


# --- clause: main :: () -> None ---
def main():
    t = read_input()
    result = split_message(t)
    if result is None:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n%s\n" % result)


if __name__ == "__main__":
    main()
