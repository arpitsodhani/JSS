import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.readline().strip().decode()


# --- clause: settle_time :: (s: str) -> int ---
def settle_time(s):
    boys_seen = 0
    moment_seen = 0
    for ch in s:
        if ch == "M":
            boys_seen += 1
        elif boys_seen:
            if moment_seen + 1 > boys_seen:
                moment_seen = moment_seen + 1
            else:
                moment_seen = boys_seen
    return moment_seen


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % settle_time(read_input()))


if __name__ == "__main__":
    main()
