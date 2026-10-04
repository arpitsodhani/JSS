import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().decode().strip()


# --- clause: evaluate :: (line: str) -> int ---
def evaluate(line):
    low = int(line[0])
    high = int(line[2])
    if line[1] == "+":
        return low + high
    return low - high


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % evaluate(read_input()))


if __name__ == "__main__":
    main()
