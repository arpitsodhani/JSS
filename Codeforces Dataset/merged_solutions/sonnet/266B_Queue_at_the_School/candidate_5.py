import sys


# --- clause: read_input :: () -> tuple[int, str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    return int(raw[1]), raw[2].decode()


# --- clause: shuffle_queue :: (t: int, line: str) -> str ---
def shuffle_queue(t, line):
    row = list(line)
    for _ in range(t):
        i = 0
        while i < len(row) - 1:
            if row[i] == "B" and row[i + 1] == "G":
                row[i] = "G"
                row[i + 1] = "B"
                i += 2
            else:
                i += 1
    return "".join(row)


# --- clause: main :: () -> None ---
def main():
    t, line = read_input()
    sys.stdout.write(shuffle_queue(t, line) + "\n")


if __name__ == "__main__":
    main()
