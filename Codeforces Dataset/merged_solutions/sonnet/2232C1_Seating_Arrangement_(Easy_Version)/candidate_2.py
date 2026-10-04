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
    opened = 0
    seated = 0
    movable = 0
    for person in line:
        if person == "I":
            if opened < x:
                opened += 1
                seated += 1
            continue
        if opened * s == seated and movable and opened < x:
            opened += 1
            movable -= 1
        if opened * s > seated:
            seated += 1
            if person == "A":
                movable += 1
        elif person == "A" and opened < x:
            opened += 1
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
