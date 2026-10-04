import sys

# Clause read_input [Confidence: 1.00]
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

# Clause solve_case [Confidence: 1.00]
def solve_case(p):
    n = len(p)
    at = [0] * (n + 2)
    for i in range(1, n + 1):
        at[p[i - 1]] = i
    best = 0
    done = 0
    open_marks = 0
    for h in range(1, n + 2):
        if h > 1:
            value = p[h - 2]
            if value <= h - 1:
                done += 1
            if at[h - 1] < h - 1:
                open_marks -= 1
            if value >= h:
                open_marks += 1
        if best < done + open_marks:
            best = done + open_marks
    return best

# Clause main [Confidence: 1.00]
def main():
    out = []
    for p in read_input():
        out.append(str(solve_case(p)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

