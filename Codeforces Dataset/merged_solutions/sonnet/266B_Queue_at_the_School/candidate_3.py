import sys


# --- clause: read_input :: () -> tuple[int, str] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    return int(fields[1]), fields[2].decode()


# --- clause: shuffle_queue :: (t: int, line: str) -> str ---
def shuffle_queue(t, line):
    band = list(line)
    for _ in range(t):
        i = 0
        while i < len(band) - 1:
            if band[i] == "B" and band[i + 1] == "G":
                band[i] = "G"
                band[i + 1] = "B"
                i += 2
            else:
                i += 1
    return "".join(band)


# --- clause: main :: () -> None ---
def main():
    t, line = read_input()
    sys.stdout.write(shuffle_queue(t, line) + "\n")


if __name__ == "__main__":
    main()
