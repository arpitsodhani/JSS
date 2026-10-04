import sys


# --- clause: read_input :: () -> str ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    return fields[1].decode()


# --- clause: decode :: (s: str) -> str ---
def decode(s):
    digits = []
    run = 0
    for ch in s:
        if ch == "1":
            run += 1
        else:
            digits.append(str(run))
            run = 0
    digits.append(str(run))
    return "".join(digits)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(decode(read_input()) + "\n")


if __name__ == "__main__":
    main()
