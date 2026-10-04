import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, str]] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    reader = 1
    cases = []
    for _ in range(t):
        c0 = int(raw[reader + 1])
        c1 = int(raw[reader + 2])
        h = int(raw[reader + 3])
        s = raw[reader + 4].decode()
        reader += 5
        cases.append((c0, c1, h, s))
    return cases


# --- clause: least_price :: (c0: int, c1: int, h: int, s: str) -> int ---
def least_price(c0, c1, h, s):
    zero = c0 if c0 < c1 + h else c1 + h
    one = c1 if c1 < c0 + h else c0 + h
    amount = 0
    for ch in s:
        amount += zero if ch == "0" else one
    return amount


# --- clause: main :: () -> None ---
def main():
    out = []
    for c0, c1, h, s in read_input():
        out.append(least_price(c0, c1, h, s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
