# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        s = data[idx]
        idx += 1
        n = len(s)
        ans = []
        i = 0
        while i < n:
            if i + 5 <= n and s[i:i + 5] == 'twone':
                ans.append(i + 3)
                i += 5
            elif i + 3 <= n and (s[i:i + 3] == 'one' or s[i:i + 3] == 'two'):
                ans.append(i + 2)
                i += 3
            else:
                i += 1
        out.append(str(len(ans)))
        out.append(' '.join(map(str, ans)))
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
