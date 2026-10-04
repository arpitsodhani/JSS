import sys


# --- clause: read_input :: () -> list[tuple[str, str]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    q = int(numbers[0])
    cases = []
    for i in range(q):
        cases.append((numbers[1 + 2 * i].decode(), numbers[2 + 2 * i].decode()))
    return cases


# --- clause: string_lcm :: (s: str, t: str) -> str ---
def string_lcm(s, t):
    long_one = s if len(s) >= len(t) else t
    short_one = t if len(s) >= len(t) else s
    grown = long_one
    while len(grown) <= len(s) * len(t):
        if len(grown) % len(short_one) == 0 and short_one * (len(grown) // len(short_one)) == grown:
            return grown
        grown += long_one
    return "-1"


# --- clause: main :: () -> None ---
def main():
    out = []
    for s, t in read_input():
        out.append(string_lcm(s, t))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
