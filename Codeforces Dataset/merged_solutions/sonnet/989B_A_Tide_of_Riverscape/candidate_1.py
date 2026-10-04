import sys


# --- clause: read_input :: () -> tuple[int, str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[1]), data[2].decode()


# --- clause: break_period :: (p: int, s: str) -> str | None ---
def break_period(p, s):
    row = list(s)
    n = len(row)
    for i in range(n - p):
        a = row[i]
        b = row[i + p]
        if a != "." and b != "." and a != b:
            broken = True
        elif a == "." and b == ".":
            row[i] = "0"
            row[i + p] = "1"
        elif a == ".":
            row[i] = "1" if b == "0" else "0"
        elif b == ".":
            row[i + p] = "1" if a == "0" else "0"
        else:
            continue
        for j in range(n):
            if row[j] == ".":
                row[j] = "0"
        return "".join(row)
    return None


# --- clause: main :: () -> None ---
def main():
    p, s = read_input()
    answer = break_period(p, s)
    sys.stdout.write("No\n" if answer is None else answer + "\n")


if __name__ == "__main__":
    main()
