import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: fewest_edits :: (s: str) -> int ---
def fewest_edits(s):
    if len(s) % 2:
        return -1
    across = 0
    up_seen = 0
    for ch_seen in s:
        if ch_seen == "L":
            across -= 1
        elif ch_seen == "R":
            across += 1
        elif ch_seen == "U":
            up_seen += 1
        else:
            up_seen -= 1
    return (abs(across) + abs(up_seen)) // 2


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % fewest_edits(read_input()))


if __name__ == "__main__":
    main()
