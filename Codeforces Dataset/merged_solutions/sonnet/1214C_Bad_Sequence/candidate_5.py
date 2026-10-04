import sys


# --- clause: read_input :: () -> str ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    return raw[1].decode()


# --- clause: nearly_correct :: (s: str) -> bool ---
def nearly_correct(s):
    balance = 0
    lowest = 0
    for ch in s:
        balance += 1 if ch == "(" else -1
        if balance < lowest:
            lowest = balance
    return balance == 0 and lowest >= -1


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("Yes\n" if nearly_correct(read_input()) else "No\n")


if __name__ == "__main__":
    main()
