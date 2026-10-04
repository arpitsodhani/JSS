import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        x = int(data[pos + 1])
        s = int(data[pos + 2])
        line = data[pos + 3].decode()
        pos += 4
        cases.append((n, x, s, line))
    return cases


# --- clause: seat_people :: (n: int, x: int, s: int, line: str) -> int ---
def seat_people(n, x, s, line):
    tables = 0
    seated = 0
    spare = 0
    for person in line:
        empty = tables * s - seated
        if person == "I":
            if tables < x:
                tables += 1
                seated += 1
        elif person == "E":
            if empty == 0 and spare > 0 and tables < x:
                tables += 1
                spare -= 1
                empty = tables * s - seated
            if empty > 0:
                seated += 1
        else:
            if empty == 0 and spare > 0 and tables < x:
                tables += 1
                spare -= 1
                empty = tables * s - seated
            if empty > 0:
                seated += 1
                spare += 1
            elif tables < x:
                tables += 1
                seated += 1
    return seated

# --- clause: main :: () -> None ---
def main():
    out = []
    for n, x, s, line in read_input():
        out.append(str(seat_people(n, x, s, line)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
