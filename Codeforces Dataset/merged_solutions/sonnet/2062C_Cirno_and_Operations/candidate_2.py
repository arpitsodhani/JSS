import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    values = list(map(int, sys.stdin.buffer.read().split()))
    ptr = 0
    tests = values[ptr]
    ptr += 1
    cases = []
    for _ in range(tests):
        n = values[ptr]
        ptr += 1
        arr = values[ptr:ptr + n]
        ptr += n
        cases.append(arr)
    return cases


# --- clause: solve_case :: (a: list[int]) -> int ---
def solve_case(a):
    seq = list(a)
    best = sum(seq)
    while len(seq) > 1:
        nxt = []
        for i in range(1, len(seq)):
            nxt.append(seq[i] - seq[i - 1])
        seq = nxt
        total = abs(sum(seq))
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
