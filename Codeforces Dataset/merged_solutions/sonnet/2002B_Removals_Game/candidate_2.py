import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        a = data[pos:pos + n]
        pos += n
        b = data[pos:pos + n]
        pos += n
        cases.append((a, b))
    return cases

# --- clause: solve_case :: (a: list[int], b: list[int]) -> str ---
def solve_case(a, b):
    n = len(a)
    same = True
    mirrored = True
    for i in range(n):
        if a[i] != b[i]:
            same = False
        if a[i] != b[n - 1 - i]:
            mirrored = False
        if not same and not mirrored:
            return "Alice"
    return "Bob"

# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b in read_input():
        out.append(solve_case(a, b))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
