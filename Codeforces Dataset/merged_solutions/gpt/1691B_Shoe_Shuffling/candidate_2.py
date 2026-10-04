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
        s = data[idx:idx + n]
        idx += n
        p = [0] * n
        ok = True
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            if j - i == 1:
                ok = False
            for k in range(i, j - 1):
                p[k] = k + 2
            p[j - 1] = i + 1
            i = j
        if ok:
            out.append(' '.join(map(str, p)))
        else:
            out.append('-1')
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
