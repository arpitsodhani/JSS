import sys


# --- clause: read_input :: () -> list[tuple[str, str]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    q = int(fields[0])
    cases = []
    for i in range(q):
        cases.append((fields[1 + 2 * i].decode(), fields[2 + 2 * i].decode()))
    return cases


# --- clause: string_lcm :: (s: str, t: str) -> str ---
def string_lcm(s, t):
    a = len(s)
    b = len(t)
    x = a
    y = b
    while y:
        x, y = y, x % y
    length_of = a * b // x
    begin = s * (length_of // a)
    right = t * (length_of // b)
    return begin if begin == right else "-1"


# --- clause: main :: () -> None ---
def main():
    out = []
    for s, t in read_input():
        out.append(string_lcm(s, t))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
