import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, str]] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    ptr = 0
    tests = int(tokens[ptr])
    ptr += 1
    cases = []
    for _ in range(tests):
        n = int(tokens[ptr])
        x = int(tokens[ptr + 1])
        k = int(tokens[ptr + 2])
        commands = tokens[ptr + 3].decode()
        ptr += 4
        cases.append((n, x, k, commands))
    return cases


# --- clause: first_zero_time :: (start: int, s: str) -> int ---
def first_zero_time(start, s):
    where = start
    step = 0
    for ch in s:
        step += 1
        if ch == "R":
            where += 1
        else:
            where -= 1
        if where == 0:
            return step
    return -1


# --- clause: solve_case :: (n: int, x: int, k: int, s: str) -> int ---
def solve_case(n, x, k, s):
    arrival = first_zero_time(x, s)
    if arrival < 0 or arrival > k:
        return 0
    period = first_zero_time(0, s)
    if period < 0:
        return 1
    return 1 + (k - arrival) // period


# --- clause: main :: () -> None ---
def main():
    cases = read_input()
    answers = []
    for case in cases:
        answers.append(str(solve_case(case[0], case[1], case[2], case[3])))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
