import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().decode().strip()


# --- clause: evaluate :: (line: str) -> int ---
def evaluate(line):
    if "+" in line:
        parts = line.split("+")
        return int(parts[0]) + int(parts[1])
    parts = line.split("-")
    return int(parts[0]) - int(parts[1])


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % evaluate(read_input()))


if __name__ == "__main__":
    main()
