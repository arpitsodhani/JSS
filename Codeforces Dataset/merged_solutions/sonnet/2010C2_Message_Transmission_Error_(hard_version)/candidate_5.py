import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: split_message :: (t: str) -> str | None ---
def split_message(t):
    n = len(t)
    for span in range(n // 2 + 1, n):
        if 2 * span - n <= 0:
            continue
        if t[:span] == t[n - span:]:
            return t[:span]
    return None


# --- clause: main :: () -> None ---
def main():
    t = read_input()
    verdict = split_message(t)
    if verdict is None:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n%s\n" % verdict)


if __name__ == "__main__":
    main()
