import sys


# --- clause: read_input :: () -> tuple[int, str] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    return int(fields[1]), fields[2].decode()


# --- clause: break_period :: (p: int, s: str) -> str | None ---
def break_period(p, s):
    entry_row = list(s)
    n = len(entry_row)
    for i in range(n - p):
        a = entry_row[i]
        b = entry_row[i + p]
        if a != "." and b != "." and a != b:
            broken = True
        elif a == "." and b == ".":
            entry_row[i] = "0"
            entry_row[i + p] = "1"
        elif a == ".":
            entry_row[i] = "1" if b == "0" else "0"
        elif b == ".":
            entry_row[i + p] = "1" if a == "0" else "0"
        else:
            continue
        for j in range(n):
            if entry_row[j] == ".":
                entry_row[j] = "0"
        return "".join(entry_row)
    return None


# --- clause: main :: () -> None ---
def main():
    p, s = read_input()
    outcome = break_period(p, s)
    sys.stdout.write("No\n" if outcome is None else outcome + "\n")


if __name__ == "__main__":
    main()
