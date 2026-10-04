import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: count_shifts :: (s: str) -> int ---
def count_shifts(s):
    n = len(s)
    doubled = s + s
    period = n
    for step in range(1, n + 1):
        if doubled[step:step + n] == s:
            period = step
            break
    return period


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % count_shifts(read_input()))


if __name__ == "__main__":
    main()
