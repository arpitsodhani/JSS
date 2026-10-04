# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
def int_iter():
    data = sys.stdin.buffer.read()
    num = 0
    in_num = False
    for b in data:
        if 48 <= b <= 57:
            num = num * 10 + (b - 48)
            in_num = True
        elif in_num:
            yield num
            num = 0
            in_num = False
    if in_num:
        yield num

def main():
    it = int_iter()
    t = next(it)
    out = []

    for _ in range(t):
        n = next(it)
        arrays = []
        mexes = []
        next_missing = []
        remove_sums = []
        total_mex = 0

        for _ in range(n):
            length = next(it)
            arr = [next(it) for _ in range(length)]
            arrays.append(arr)

            freq = [0] * (length + 2)
            for x in arr:
                if x <= length + 1:
                    freq[x] += 1

            mex = 0
            while freq[mex]:
                mex += 1

            nxt = mex + 1
            while freq[nxt]:
                nxt += 1

            rem_sum = length * mex
            for x in range(mex):
                if freq[x] == 1:
                    rem_sum += x - mex

            mexes.append(mex)
            next_missing.append(nxt)
            remove_sums.append(rem_sum)
            total_mex += mex

        delta = defaultdict(int)
        for mex, nxt in zip(mexes, next_missing):
            delta[mex] += nxt - mex

        ans = 0
        multiplier = n - 1

        for arr, mex, rem_sum in zip(arrays, mexes, remove_sums):
            ans += multiplier * (len(arr) * (total_mex - mex) + rem_sum)
            for x in arr:
                ans += delta.get(x, 0)

        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
