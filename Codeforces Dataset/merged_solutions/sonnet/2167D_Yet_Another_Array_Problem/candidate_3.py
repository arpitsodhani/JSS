import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        offset += 1
        cases.append(fields[offset:offset + n])
        offset += n
    return cases


# --- clause: gcd_of :: (a: int, b: int) -> int ---
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a


# --- clause: smallest_coprime :: (a: list[int]) -> int ---
def smallest_coprime(a):
    for x in range(2, 200):
        for entry in a:
            if gcd_of(entry, x) == 1:
                return x
    return -1


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(smallest_coprime(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
