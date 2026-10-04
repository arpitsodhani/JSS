# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def enough_tvs(intervals):
    starts = sorted(l for l, _ in intervals)
    ends = sorted(r for _, r in intervals)
    i = 0
    j = 0
    active = 0
    n = len(intervals)
    while i < n:
        if j == n or starts[i] <= ends[j]:
            active += 1
            i += 1
            if active > 2:
                return False
        else:
            active -= 1
            j += 1
    return True

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return
    n = values[0]
    intervals = [(values[i], values[i + 1]) for i in range(1, 2 * n, 2)]
    sys.stdout.write("YES" if enough_tvs(intervals) else "NO")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
