import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: split_message :: (t: str) -> str | None ---
def split_message(t):
    n = len(t)
    size = n - 1
    while size > n // 2:
        overlap = 2 * size - n
        if overlap > 0 and t[:size] == t[n - size:]:
            return t[:size]
        size -= 1
    return None


# --- clause: main :: () -> None ---
def main():
    t = read_input()
    outcome = split_message(t)
    if outcome is None:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n%s\n" % outcome)


if __name__ == "__main__":
    main()
