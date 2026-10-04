import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [(int(data[3 * i + 1]), int(data[3 * i + 2]), int(data[3 * i + 3]))
            for i in range(t)]


# --- clause: solve_case :: (a: int, b: int, c: int) -> int ---
def solve_case(a, b, c):
    if (a + b + c) % 3:
        return 1
    return 0


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(str(solve_case(case[0], case[1], case[2])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
