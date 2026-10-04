import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: fewest_edits :: (s: str) -> int ---
def fewest_edits(s):
    if len(s) % 2:
        return -1
    across = 0
    up_value = 0
    for ch_value in s:
        if ch_value == "L":
            across -= 1
        elif ch_value == "R":
            across += 1
        elif ch_value == "U":
            up_value += 1
        else:
            up_value -= 1
    return (abs(across) + abs(up_value)) // 2


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % fewest_edits(read_input()))


if __name__ == "__main__":
    main()
