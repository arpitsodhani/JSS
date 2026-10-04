import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    idx = 1
    total = int(data[0])
    cases = []
    for _ in range(total):
        h, p = int(data[idx]), int(data[idx + 1])
        idx += 2
        cases.append((h, p))
    return cases


# --- clause: solve_case :: (h: int, p: int) -> int ---
def solve_case(h, p):
    level = 0
    while level < h and (1 << level) <= p:
        level = level + 1
    left = (1 << h) - (1 << level)
    steps = (left + p - 1) // p
    return level + steps


# --- clause: main :: () -> None ---
def main():
    answers = []
    for h, p in read_input():
        answers.append(str(solve_case(h, p)))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
