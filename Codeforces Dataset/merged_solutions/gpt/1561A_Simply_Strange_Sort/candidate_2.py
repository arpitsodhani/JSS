# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    idx = 1
    ans = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        cnt = 0
        while a != sorted(a):
            cnt += 1
            start = 0 if cnt % 2 == 1 else 1
            for i in range(start, n - 1, 2):
                if a[i] > a[i + 1]:
                    a[i], a[i + 1] = (a[i + 1], a[i])
        ans.append(str(cnt))
    print('\n'.join(ans))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
