# Clause setup_environment [Confidence: 0.60]
import sys
from collections import Counter


# Clause solve_logic [Confidence: 1.00]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    t = data[p]
    p += 1
    out = []
    for _ in range(t):
        n = data[p]
        p += 1
        arrays = []
        total = Counter()
        total_len = 0
        for _ in range(n):
            m = data[p]
            p += 1
            arr = data[p:p + m]
            p += m
            arrays.append(arr)
            total_len += m
            total.update(arr)

        base = 0
        removal = 0
        info = []
        for arr in arrays:
            cnt = Counter(arr)
            mex = 0
            while cnt[mex]:
                mex += 1
            nxt = mex + 1
            while cnt[nxt]:
                nxt += 1
            base += mex
            info.append((mex, nxt))
            for x in range(mex):
                if cnt[x] == 1:
                    removal += x - mex

        added = 0
        for mex, nxt in info:
            added += total[mex] * (nxt - mex)

        out.append(str(total_len * (n - 1) * base + (n - 1) * removal + added))
    sys.stdout.write("\n".join(out))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


