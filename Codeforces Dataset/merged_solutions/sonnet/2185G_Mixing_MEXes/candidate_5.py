# CLAUSE: setup_environment
import sys
from collections import Counter

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    i = 0
    tests = data[i]
    i += 1
    ans = []

    for _ in range(tests):
        n = data[i]
        i += 1
        total = Counter()
        local_infos = []
        total_len = 0
        base = 0
        removal = 0

        for _ in range(n):
            m = data[i]
            i += 1
            arr = data[i:i + m]
            i += m
            total_len += m
            total.update(arr)

            limit = m + 2
            freq = [0] * (limit + 1)
            for value in arr:
                if 0 <= value <= limit:
                    freq[value] += 1

            mex = 0
            while freq[mex] > 0:
                mex += 1

            nxt = mex + 1
            while nxt <= limit and freq[nxt] > 0:
                nxt += 1

            base += mex
            for value in range(mex):
                if freq[value] == 1:
                    removal += value - mex
            local_infos.append((mex, nxt))

        gain = 0
        for mex, nxt in local_infos:
            gain += total[mex] * (nxt - mex)

        ans.append(str(total_len * (n - 1) * base + (n - 1) * removal + gain))

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
