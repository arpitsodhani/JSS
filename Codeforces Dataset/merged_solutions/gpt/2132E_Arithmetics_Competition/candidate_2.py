# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    t = next(it)
    out = []
    for _ in range(t):
        n = next(it)
        m = next(it)
        q = next(it)
        a = [next(it) for _ in range(n)]
        b = [next(it) for _ in range(m)]
        a.sort(reverse=True)
        b.sort(reverse=True)
        pa = [0] * (n + 1)
        for i, v in enumerate(a, 1):
            pa[i] = pa[i - 1] + v
        pb = [0] * (m + 1)
        for i, v in enumerate(b, 1):
            pb[i] = pb[i - 1] + v
        for _ in range(q):
            x = next(it)
            y = next(it)
            z = next(it)
            left = max(0, z - y)
            right = min(z, x)
            lo = left + 1
            hi = right
            first_bad = right + 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if a[mid - 1] <= b[z - mid]:
                    first_bad = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            if first_bad == right + 1:
                k = right
            else:
                k = first_bad - 1
            out.append(str(pa[k] + pb[z - k]))
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
