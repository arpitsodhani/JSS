import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    ptr = 0
    tests = data[ptr]
    ptr += 1
    cases = []
    for _ in range(tests):
        n = data[ptr]
        ptr += 1
        arr = data[ptr:ptr + n]
        ptr += n
        cases.append(arr)
    return cases


# --- clause: solve_case :: (p: list[int]) -> int ---
def solve_case(p):
    n = len(p)
    index_of = [0] * (n + 2)
    for i, v in enumerate(p, start=1):
        index_of[v] = i
    best = 0
    low = 0
    high = 0
    for h in range(1, n + 2):
        if h > 1:
            if p[h - 2] <= h - 1:
                low += 1
            if index_of[h - 1] < h - 1:
                high -= 1
            if p[h - 2] >= h:
                high += 1
        total = low + high
        if total > best:
            best = total
    return best


# --- clause: main :: () -> None ---
def main():
    cases = read_input()
    answers = []
    for arr in cases:
        answers.append(str(solve_case(arr)))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
