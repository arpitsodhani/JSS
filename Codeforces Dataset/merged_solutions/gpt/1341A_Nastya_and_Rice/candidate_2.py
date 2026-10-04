# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    ans = []
    idx = 1
    for _ in range(t):
        n, a, b, c, d = data[idx:idx + 5]
        idx += 5
        low = n * (a - b)
        high = n * (a + b)
        target_low = c - d
        target_high = c + d
        ans.append('Yes' if max(low, target_low) <= min(high, target_high) else 'No')
    print('\n'.join(ans))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
