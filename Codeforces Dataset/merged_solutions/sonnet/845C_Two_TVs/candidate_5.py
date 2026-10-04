# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    n = int(raw[0])
    pairs = []
    for i in range(n):
        left = int(raw[2 * i + 1])
        right = int(raw[2 * i + 2])
        pairs.append((left, right))
    pairs.sort()
    tv_until = [-1, -1]
    for left, right in pairs:
        if tv_until[0] < left:
            tv_until[0] = right
        elif tv_until[1] < left:
            tv_until[1] = right
        else:
            sys.stdout.write("NO")
            return
        if tv_until[0] > tv_until[1]:
            tv_until[0], tv_until[1] = tv_until[1], tv_until[0]
    sys.stdout.write("YES")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
