import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    ptr = 0
    tests = data[ptr]
    ptr += 1
    cases = []
    for _ in range(tests):
        n, m, q = data[ptr], data[ptr + 1], data[ptr + 2]
        ptr += 3
        ops = []
        for _ in range(q):
            ops.append(data[ptr])
            ptr += 1
        cases.append((n, m, ops))
    return cases


# --- clause: advance :: (segments: list[tuple[int, int]], a: int, n: int) -> list[tuple[int, int]] ---
def advance(segments, a, n):
    pieces = []
    for lo, hi in segments:
        if lo <= a and a <= hi:
            pieces.append((1, 1))
            pieces.append((n, n))
        upper = a - 1 if a - 1 < hi else hi
        if lo <= upper:
            pieces.append((lo, upper + 1))
        lower = a + 1 if a + 1 > lo else lo
        if lower <= hi:
            pieces.append((lower - 1, hi))
    pieces.sort()
    joined = []
    for lo, hi in pieces:
        if joined and lo <= joined[-1][1] + 1:
            if hi > joined[-1][1]:
                joined[-1] = (joined[-1][0], hi)
        else:
            joined.append((lo, hi))
    return joined


# --- clause: solve_case :: (n: int, m: int, ops: list[int]) -> list[int] ---
def solve_case(n, m, ops):
    state = [(m, m)]
    answer = []
    for a in ops:
        state = advance(state, a, n)
        total = 0
        for lo, hi in state:
            total += hi - lo + 1
        answer.append(total)
    return answer


# --- clause: main :: () -> None ---
def main():
    cases = read_input()
    answers = []
    for case in cases:
        values = solve_case(case[0], case[1], case[2])
        answers.append(" ".join(map(str, values)))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
