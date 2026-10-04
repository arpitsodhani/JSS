# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        seen = [False] * (k + 1)
        for x in data[idx:idx + n]:
            if x <= k:
                seen[x] = True
        idx += n
        mex = 0
        while seen[mex]:
            mex += 1
        ans.append(str(min(mex, k - 1)))
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
