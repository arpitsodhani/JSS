# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n = data[0]
    intervals = []
    idx = 1
    for _ in range(n):
        l = data[idx]
        r = data[idx + 1]
        idx += 2
        intervals.append((l, r))

    intervals.sort()

    tv1 = -1
    tv2 = -1

    for l, r in intervals:
        if l > tv1:
            tv1 = r
        elif l > tv2:
            tv2 = r
        else:
            print("NO")
            return

        if tv1 > tv2:
            tv1, tv2 = tv2, tv1

    print("YES")

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
