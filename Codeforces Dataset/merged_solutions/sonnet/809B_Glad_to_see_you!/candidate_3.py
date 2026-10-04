# CLAUSE: setup_environment
import sys

read_line = sys.stdin.readline

def query(pair):
    x, y = pair
    sys.stdout.write(f"1 {x} {y}\n")
    sys.stdout.flush()
    return read_line().strip() == "TAK"

# CLAUSE: solve_logic
def first_true_position(lo, hi):
    span = hi - lo
    while span:
        step = span // 2
        mid = lo + step
        if query((mid, mid + 1)):
            span = step
        else:
            lo = mid + 1
            span -= step + 1
    return lo

def solve():
    start = read_line().split()
    if len(start) == 0:
        return
    n = int(start[0])
    main_point = first_true_position(1, n)
    answer = [main_point, -1]
    if main_point != 1:
        left_point = first_true_position(1, main_point - 1)
        if query((left_point, main_point)):
            answer[1] = left_point
    if answer[1] == -1 and main_point != n:
        answer[1] = first_true_position(main_point + 1, n)
    sys.stdout.write("2 {} {}\n".format(answer[0], answer[1]))
    sys.stdout.flush()

# CLAUSE: finish_program
if __name__ == "__main__":
    solve()
