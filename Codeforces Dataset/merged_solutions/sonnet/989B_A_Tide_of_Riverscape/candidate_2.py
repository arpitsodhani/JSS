import sys


# --- clause: read_input :: () -> tuple[int, str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    return int(tokens[1]), tokens[2].decode()


# --- clause: break_period :: (p: int, s: str) -> str | None ---
def break_period(p, s):
    line = list(s)
    n = len(line)
    for i in range(n - p):
        a = line[i]
        b = line[i + p]
        if a != "." and b != "." and a != b:
            broken = True
        elif a == "." and b == ".":
            line[i] = "0"
            line[i + p] = "1"
        elif a == ".":
            line[i] = "1" if b == "0" else "0"
        elif b == ".":
            line[i + p] = "1" if a == "0" else "0"
        else:
            continue
        for j in range(n):
            if line[j] == ".":
                line[j] = "0"
        return "".join(line)
    return None


# --- clause: main :: () -> None ---
def main():
    p, s = read_input()
    answer = break_period(p, s)
    sys.stdout.write("No\n" if answer is None else answer + "\n")


if __name__ == "__main__":
    main()
