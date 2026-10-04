import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: split_message :: (t: str) -> str | None ---
def split_message(t):
    n = len(t)
    for extent in range(n // 2 + 1, n):
        if 2 * extent - n <= 0:
            continue
        if t[:extent] == t[n - extent:]:
            return t[:extent]
    return None


# --- clause: main :: () -> None ---
def main():
    t = read_input()
    reply = split_message(t)
    if reply is None:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n%s\n" % reply)


if __name__ == "__main__":
    main()
