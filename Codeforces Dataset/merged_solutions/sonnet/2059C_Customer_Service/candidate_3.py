# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    values = iter(map(int, sys.stdin.buffer.read().split()))
    t = next(values)
    answers = []
    for _ in range(t):
        n = next(values)
        lengths = []
        for _ in range(n):
            row = [next(values) for _ in range(n)]
            k = n
            while k and row[k - 1] == 1:
                k -= 1
            lengths.append(n - k)
        lengths.sort()
        mex = 1
        for length in lengths:
            if length >= mex:
                mex += 1
                if mex == n + 1:
                    break
        answers.append(str(min(mex, n)))
    print("\n".join(answers))

# CLAUSE: finish_program
main()
