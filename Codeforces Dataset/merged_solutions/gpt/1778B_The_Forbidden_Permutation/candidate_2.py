# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, m, d = (data[idx], data[idx + 1], data[idx + 2])
        idx += 3
        p = data[idx:idx + n]
        idx += n
        a = data[idx:idx + m]
        idx += m
        pos = [0] * (n + 1)
        for i, x in enumerate(p):
            pos[x] = i
        ans = 10 ** 18
        for i in range(m - 1):
            l = pos[a[i]]
            r = pos[a[i + 1]]
            if l > r or r - l > d:
                ans = 0
                break
            diff = r - l
            ans = min(ans, diff)
            need = d - diff + 1
            if l + (n - 1 - r) >= need:
                ans = min(ans, need)
        out.append(str(ans))
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
