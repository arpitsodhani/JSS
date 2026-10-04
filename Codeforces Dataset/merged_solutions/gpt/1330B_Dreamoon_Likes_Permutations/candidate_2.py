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
        a = data[idx:idx + n]
        idx += n
        pref = [False] * (n + 1)
        suff = [False] * (n + 2)
        seen = set()
        mx = 0
        ok = True
        for i in range(1, n + 1):
            v = a[i - 1]
            if v in seen:
                ok = False
            seen.add(v)
            if v > mx:
                mx = v
            if ok and mx == i:
                pref[i] = True
        seen.clear()
        mx = 0
        ok = True
        for i in range(n, 0, -1):
            v = a[i - 1]
            if v in seen:
                ok = False
            seen.add(v)
            if v > mx:
                mx = v
            length = n - i + 1
            if ok and mx == length:
                suff[i] = True
        ans = []
        for l1 in range(1, n):
            if pref[l1] and suff[l1 + 1]:
                ans.append((l1, n - l1))
        out.append(str(len(ans)))
        for x, y in ans:
            out.append(f'{x} {y}')
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
