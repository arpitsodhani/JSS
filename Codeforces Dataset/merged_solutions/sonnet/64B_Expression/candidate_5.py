import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().decode().strip()


# --- clause: evaluate :: (line: str) -> int ---
def evaluate(line):
    first_side = int(line[0])
    second_side = int(line[2])
    if line[1] == "+":
        return first_side + second_side
    return first_side - second_side


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % evaluate(read_input()))


if __name__ == "__main__":
    main()
