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
    forward = all(x == y for x, y in zip(a, b))
    backward = all(x == y for x, y in zip(a, reversed(b)))
    return "Bob" if forward or backward else "Alice"

# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b in read_input():
        out.append(solve_case(a, b))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
