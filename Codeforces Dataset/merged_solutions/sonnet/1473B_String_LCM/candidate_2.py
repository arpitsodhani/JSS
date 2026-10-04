import sys


# --- clause: read_input :: () -> list[tuple[str, str]] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    q = int(tokens[0])
    cases = []
    for i in range(q):
        cases.append((tokens[1 + 2 * i].decode(), tokens[2 + 2 * i].decode()))
    return cases


# --- clause: string_lcm :: (s: str, t: str) -> str ---
def string_lcm(s, t):
    a = len(s)
    b = len(t)
    x = a
    y = b
    while y:
        x, y = y, x % y
    size = a * b // x
    low = s * (size // a)
    right = t * (size // b)
    return low if low == right else "-1"


# --- clause: main :: () -> None ---
def main():
    out = []
    for s, t in read_input():
        out.append(string_lcm(s, t))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
