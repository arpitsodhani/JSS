import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.readline().strip().decode()


# --- clause: settle_time :: (s: str) -> int ---
def settle_time(s):
    boys_value = 0
    moment_value = 0
    for ch in s:
        if ch == "M":
            boys_value += 1
        elif boys_value:
            if moment_value + 1 > boys_value:
                moment_value += 1
            else:
                moment_value = boys_value
    return moment_value


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % settle_time(read_input()))


if __name__ == "__main__":
    main()
