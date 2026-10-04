# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    input = sys.stdin.readline
    n = int(input())
    s = input().strip()
    a = list(map(int, input().split()))
    target = 'hard'
    inf = 10 ** 30
    dp = [0, inf, inf, inf]
    for ch, cost in zip(s, a):
        ndp = [inf] * 4
        for j in range(4):
            if dp[j] == inf:
                continue
            ndp[j] = min(ndp[j], dp[j] + cost)
            if ch == target[j]:
                if j + 1 < 4:
                    ndp[j + 1] = min(ndp[j + 1], dp[j])
            else:
                ndp[j] = min(ndp[j], dp[j])
        dp = ndp
    print(min(dp))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
