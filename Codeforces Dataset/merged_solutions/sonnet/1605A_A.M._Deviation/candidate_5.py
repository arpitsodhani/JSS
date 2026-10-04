import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        triple = tuple(int(token) for token in data[pos:pos + 3])
        pos += 3
        cases.append(triple)
    return cases


# --- clause: solve_case :: (a: int, b: int, c: int) -> int ---
def solve_case(a, b, c):
    spare = (a + b + c) - 3 * ((a + b + c) // 3)
    return 1 if spare else 0


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b, c in read_input():
        out.append(str(solve_case(a, b, c)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
