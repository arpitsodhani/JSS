# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    q = data[0]
    at = 1
    out = []
    for _ in range(q):
        n = data[at]
        at += 1
        counts = [0] * (n + 2)
        for x in data[at:at + n]:
            if x <= n:
                counts[x] += 1
        at += n
        total = 0
        for need in (1, 2):
            mex = 0
            while mex <= n and counts[mex] >= need:
                mex += 1
            total += mex
        out.append(str(total))

# CLAUSE: finish_program
    print("\n".join(out))

if __name__ == "__main__":
    main()
