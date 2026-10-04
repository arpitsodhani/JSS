import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.readline().strip().decode()


# --- clause: settle_time :: (s: str) -> int ---
def settle_time(s):
    boys_so_far = 0
    moment_so_far = 0
    for ch in s:
        if ch == "M":
            boys_so_far += 1
        elif boys_so_far:
            if moment_so_far + 1 > boys_so_far:
                moment_so_far = moment_so_far + 1
            else:
                moment_so_far = boys_so_far
    return moment_so_far


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % settle_time(read_input()))


if __name__ == "__main__":
    main()
