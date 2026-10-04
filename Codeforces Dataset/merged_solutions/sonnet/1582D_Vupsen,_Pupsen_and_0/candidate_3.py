import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        cursor += 1
        cases.append(fields[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: build_partner :: (a: list[int]) -> list[int] ---
def build_partner(a):
    n = len(a)
    b = [0] * n
    opening = 0
    if n % 2:
        x, y, z = a[0], a[1], a[2]
        if x + y != 0:
            b[0] = z
            b[1] = z
            b[2] = -(x + y)
        elif x + z != 0:
            b[0] = y
            b[2] = y
            b[1] = -(x + z)
        else:
            b[1] = x
            b[2] = x
            b[0] = -(y + z)
        opening = 3
    for i in range(opening, n, 2):
        b[i] = a[i + 1]
        b[i + 1] = -a[i]
    return b


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(" ".join(map(str, build_partner(a))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
