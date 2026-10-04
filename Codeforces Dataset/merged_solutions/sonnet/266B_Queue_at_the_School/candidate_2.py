import sys


# --- clause: read_input :: () -> tuple[int, str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    return int(tokens[1]), tokens[2].decode()


# --- clause: shuffle_queue :: (t: int, line: str) -> str ---
def shuffle_queue(t, line):
    record = list(line)
    for _ in range(t):
        i = 0
        while i < len(record) - 1:
            if record[i] == "B" and record[i + 1] == "G":
                record[i] = "G"
                record[i + 1] = "B"
                i += 2
            else:
                i += 1
    return "".join(record)


# --- clause: main :: () -> None ---
def main():
    t, line = read_input()
    sys.stdout.write(shuffle_queue(t, line) + "\n")


if __name__ == "__main__":
    main()
