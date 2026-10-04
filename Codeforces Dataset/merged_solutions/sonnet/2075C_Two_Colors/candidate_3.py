# CLAUSE: setup_environment
import sys

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    tests = values[p]
    p += 1
    answers = []

# CLAUSE: solve_logic
    for _ in range(tests):
        n = values[p]
        m = values[p + 1]
        p += 2
        freq = [0] * (n + 1)
        for x in values[p:p + m]:
            if x >= n:
                freq[n] += 1
            else:
                freq[x] += 1
        p += m
        enough = [0] * (n + 2)
        run = 0
        for i in range(n, 0, -1):
            run += freq[i]
            enough[i] = run
        ans = 0
        for left in range(1, n):
            right = n - left
            same_need = left if left > right else right
            ans += enough[left] * enough[right] - enough[same_need]
        answers.append(str(ans))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    main()
