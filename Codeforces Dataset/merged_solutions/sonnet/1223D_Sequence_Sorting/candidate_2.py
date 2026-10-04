import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    ptr = 0
    queries = data[ptr]
    ptr += 1
    cases = []
    for _ in range(queries):
        n = data[ptr]
        ptr += 1
        arr = data[ptr:ptr + n]
        ptr += n
        cases.append(arr)
    return cases


# --- clause: solve_case :: (a: list[int]) -> int ---
def solve_case(a):
    n = len(a)
    start = [-1] * (n + 1)
    stop = [-1] * (n + 1)
    for i, v in enumerate(a):
        if start[v] < 0:
            start[v] = i
        stop[v] = i
    keys = [v for v in range(1, n + 1) if start[v] >= 0]
    best = 1
    run = 1
    for j in range(1, len(keys)):
        if stop[keys[j - 1]] < start[keys[j]]:
            run += 1
        else:
            run = 1
        if run > best:
            best = run
    return len(keys) - best


# --- clause: main :: () -> None ---
def main():
    cases = read_input()
    answers = []
    for arr in cases:
        answers.append(str(solve_case(arr)))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
