# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        pref = 0
        b = []
        for i in range(1, n + 1):
            b.append((pref, i))
            pref += data[idx]
            idx += 1
        b.sort()
        ans = [0] * n
        val = n
        for _, pos in b:
            ans[pos - 1] = val
            val -= 1
        out.append(' '.join(map(str, ans)))
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
