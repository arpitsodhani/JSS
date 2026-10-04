import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.readline().strip().decode()


# --- clause: settle_time :: (s: str) -> int ---
def settle_time(s):
    boys = 0
    moment = 0
    for ch in s:
        if ch == "M":
            boys += 1
        elif boys:
            if moment + 1 > boys:
                moment = moment + 1
            else:
                moment = boys
    return moment


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % settle_time(read_input()))


if __name__ == "__main__":
    main()
