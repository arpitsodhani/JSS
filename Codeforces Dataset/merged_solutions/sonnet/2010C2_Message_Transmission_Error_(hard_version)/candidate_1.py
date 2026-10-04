import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: split_message :: (t: str) -> str | None ---
def split_message(t):
    n = len(t)
    for size in range(n // 2 + 1, n):
        if 2 * size - n <= 0:
            continue
        if t[:size] == t[n - size:]:
            return t[:size]
    return None


# --- clause: main :: () -> None ---
def main():
    t = read_input()
    answer = split_message(t)
    if answer is None:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n%s\n" % answer)


if __name__ == "__main__":
    main()
