import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    numbers = list(map(int, data[1:1 + 3 * t]))
    return list(zip(numbers[0::3], numbers[1::3], numbers[2::3]))


# --- clause: solve_case :: (a: int, b: int, c: int) -> int ---
def solve_case(a, b, c):
    rest = (a + b + c) % 3
    if rest > 1:
        rest = 3 - rest
    return rest


# --- clause: main :: () -> None ---
def main():
    answers = []
    for a, b, c in read_input():
        answers.append(str(solve_case(a, b, c)))
    sys.stdout.write("%s\n" % "\n".join(answers))


if __name__ == "__main__":
    main()
