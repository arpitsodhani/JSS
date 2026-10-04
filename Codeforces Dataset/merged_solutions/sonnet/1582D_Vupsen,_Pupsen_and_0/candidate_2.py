import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        pos += 1
        cases.append(tokens[pos:pos + n])
        pos += n
    return cases


# --- clause: build_partner :: (a: list[int]) -> list[int] ---
def build_partner(a):
    n = len(a)
    b = [0] * n
    begin = 0
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
        begin = 3
    for i in range(begin, n, 2):
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
