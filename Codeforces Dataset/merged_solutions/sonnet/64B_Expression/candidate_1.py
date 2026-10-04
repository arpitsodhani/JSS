import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().decode().strip()


# --- clause: evaluate :: (line: str) -> int ---
def evaluate(line):
    left = int(line[0])
    right = int(line[2])
    if line[1] == "+":
        return left + right
    return left - right


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % evaluate(read_input()))


if __name__ == "__main__":
    main()
