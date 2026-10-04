# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    values = data[1:1 + n]
    total = 0
    minimum_time = 0

    for i, value in enumerate(values, 1):
        total += value
        need_time = (total + i - 1) // i
        if need_time > minimum_time:
            minimum_time = need_time

    q_index = 1 + n
    q = data[q_index]
    queries = data[q_index + 1:q_index + 1 + q]

    out = []
    for t in queries:
        if t < minimum_time:
            out.append("-1")
        else:
            out.append(str((total + t - 1) // t))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
