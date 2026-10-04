import sys
from math import gcd


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases

# --- clause: solve_case :: (b: list[int]) -> int ---
def solve_case(b):
    x = 1
    for i in range(len(b) - 1):
        left = b[i]
        right = b[i + 1]
        if left % right == 0 or right % left:
            need = left // gcd(left, right)
            x = x * need // gcd(x, need)
    return x

# --- clause: main :: () -> None ---
def main():
    out = []
    for b in read_input():
        out.append(str(solve_case(b)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
