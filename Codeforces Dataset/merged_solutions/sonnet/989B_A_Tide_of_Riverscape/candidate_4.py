import sys


# --- clause: read_input :: () -> tuple[int, str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return int(numbers[1]), numbers[2].decode()


# --- clause: break_period :: (p: int, s: str) -> str | None ---
def break_period(p, s):
    n = len(s)
    spot = -1
    for i in range(n - p):
        a = s[i]
        b = s[i + p]
        if a == "." or b == "." or a != b:
            spot = i
            break
    if spot < 0:
        return None
    row = ["0" if ch == "." else ch for ch in s]
    a = s[spot]
    b = s[spot + p]
    if a == "." and b == ".":
        row[spot + p] = "1"
    elif a == ".":
        row[spot] = "1" if b == "0" else "0"
    elif b == ".":
        row[spot + p] = "1" if a == "0" else "0"
    return "".join(row)


# --- clause: main :: () -> None ---
def main():
    p, s = read_input()
    answer = break_period(p, s)
    sys.stdout.write("No\n" if answer is None else answer + "\n")


if __name__ == "__main__":
    main()
