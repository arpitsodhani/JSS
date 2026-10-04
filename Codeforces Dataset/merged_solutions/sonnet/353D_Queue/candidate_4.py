import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.readline().strip().decode()


# --- clause: settle_time :: (s: str) -> int ---
def settle_time(s):
    ahead = 0
    latest = 0
    for ch in s:
        if ch == "M":
            ahead += 1
            continue
        if ahead == 0:
            continue
        latest = max(latest + 1, ahead)
    return latest


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % settle_time(read_input()))


if __name__ == "__main__":
    main()
