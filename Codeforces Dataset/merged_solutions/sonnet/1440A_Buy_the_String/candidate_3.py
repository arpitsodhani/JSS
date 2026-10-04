import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, str]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    t = int(fields[0])
    offset = 1
    cases = []
    for _ in range(t):
        c0 = int(fields[offset + 1])
        c1 = int(fields[offset + 2])
        h = int(fields[offset + 3])
        s = fields[offset + 4].decode()
        offset += 5
        cases.append((c0, c1, h, s))
    return cases


# --- clause: least_price :: (c0: int, c1: int, h: int, s: str) -> int ---
def least_price(c0, c1, h, s):
    zero = c0 if c0 < c1 + h else c1 + h
    one = c1 if c1 < c0 + h else c0 + h
    summed = 0
    for ch in s:
        summed += zero if ch == "0" else one
    return summed


# --- clause: main :: () -> None ---
def main():
    out = []
    for c0, c1, h, s in read_input():
        out.append(least_price(c0, c1, h, s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
