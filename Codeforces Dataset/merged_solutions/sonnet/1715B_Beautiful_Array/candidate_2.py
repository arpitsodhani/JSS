import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    tests = data[0]
    ptr = 1
    cases = []
    for _ in range(tests):
        n, k, b, s = data[ptr], data[ptr + 1], data[ptr + 2], data[ptr + 3]
        cases.append((n, k, b, s))
        ptr += 4
    return cases


# --- clause: solve_case :: (n: int, k: int, b: int, s: int) -> str ---
def solve_case(n, k, b, s):
    minimum = k * b
    maximum = minimum + n * (k - 1)
    if s < minimum or s > maximum:
        return "-1"
    values = [0] * n
    first = minimum + k - 1
    if s < first:
        first = s
    values[0] = first
    left = s - first
    for i in range(1, n):
        portion = left if left < k - 1 else k - 1
        values[i] = portion
        left -= portion
    return " ".join(map(str, values))


# --- clause: main :: () -> None ---
def main():
    cases = read_input()
    answers = []
    for case in cases:
        answers.append(solve_case(case[0], case[1], case[2], case[3]))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
