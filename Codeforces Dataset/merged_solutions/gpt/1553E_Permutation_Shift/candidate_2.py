# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    input = sys.stdin.readline
    t = int(input())
    out = []
    for _ in range(t):
        n, m = map(int, input().split())
        p = list(map(int, input().split()))
        cnt = [0] * n
        for i, x in enumerate(p):
            cnt[(i - (x - 1)) % n] += 1
        ans = []
        need = n - 2 * m
        for k in range(n):
            if cnt[k] < need:
                continue
            seen = [0] * n
            cycles = 0
            for i in range(n):
                if not seen[i]:
                    cycles += 1
                    v = i
                    while not seen[v]:
                        seen[v] = 1
                        v = (p[v] - 1 + k) % n
            if n - cycles <= m:
                ans.append(k)
        out.append(str(len(ans)) + (' ' + ' '.join(map(str, ans)) if ans else ''))
    print('\n'.join(out))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
