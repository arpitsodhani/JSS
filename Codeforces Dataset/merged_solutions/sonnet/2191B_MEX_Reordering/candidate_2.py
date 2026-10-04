# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    t = nums[p]
    p += 1
    ans = []
    for _ in range(t):
        n = nums[p]
        p += 1
        arr = nums[p:p + n]
        p += n

        present = set(arr)
        mex = 0
        while mex in present:
            mex += 1

        if mex == 0:
            ans.append("YES" if n == 1 else "NO")
        else:
            freq = [0] * mex
            for v in arr:
                if 0 <= v < mex:
                    freq[v] += 1
            ans.append("YES" if min(freq) == 1 else "NO")

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
