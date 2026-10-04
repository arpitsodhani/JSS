import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    while len(cases) < t:
        n = int(data[pos])
        x = int(data[pos + 1])
        s = int(data[pos + 2])
        u = data[pos + 3]
        pos += 4
        cases.append((n, x, s, u))
    return cases


# --- clause: seat_people :: (n: int, x: int, s: int, u: bytes) -> int ---
def seat_people(n, x, s, u):
    opened = 0
    seated = 0
    fillers = 0
    for person in u:
        free = opened * s - seated
        if person == 73:
            if opened < x:
                opened += 1
                seated += 1
        elif person == 69:
            if free == 0 and fillers > 0 and opened < x:
                opened += 1
                fillers -= 1
                free = opened * s - seated
            if free > 0:
                seated += 1
        else:
            if free == 0 and fillers > 0 and opened < x:
                opened += 1
                fillers -= 1
                free = opened * s - seated
            if free == 0:
                if opened < x:
                    opened += 1
                    seated += 1
            else:
                seated += 1
                fillers += 1
    return seated


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, x, s, u in read_input():
        out.append(str(seat_people(n, x, s, u)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
