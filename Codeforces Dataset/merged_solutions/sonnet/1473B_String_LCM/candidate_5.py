import sys


# --- clause: read_input :: () -> list[tuple[str, str]] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    q = int(raw[0])
    cases = []
    for i in range(q):
        cases.append((raw[1 + 2 * i].decode(), raw[2 + 2 * i].decode()))
    return cases


# --- clause: string_lcm :: (s: str, t: str) -> str ---
def string_lcm(s, t):
    a = len(s)
    b = len(t)
    x = a
    y = b
    while y:
        x, y = y, x % y
    width = a * b // x
    first_side = s * (width // a)
    right = t * (width // b)
    return first_side if first_side == right else "-1"


# --- clause: main :: () -> None ---
def main():
    out = []
    for s, t in read_input():
        out.append(string_lcm(s, t))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
