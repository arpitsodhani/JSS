import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: fewest_edits :: (s: str) -> int ---
def fewest_edits(s):
    if len(s) % 2:
        return -1
    tally = {"L": 0, "R": 0, "U": 0, "D": 0}
    for ch in s:
        tally[ch] += 1
    across = abs(tally["L"] - tally["R"])
    up = abs(tally["U"] - tally["D"])
    return (across + up) // 2


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % fewest_edits(read_input()))


if __name__ == "__main__":
    main()
