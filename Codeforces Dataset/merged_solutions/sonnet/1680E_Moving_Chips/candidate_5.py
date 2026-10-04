# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve_case(n, top, bottom):
    left = None
    right = None

    for i, cells in enumerate(zip(top, bottom)):
        if cells[0] == "*" or cells[1] == "*":
            if left is None:
                left = i
            right = i

    top_cost = 1 if bottom[left] == "*" else 0
    bottom_cost = 1 if top[left] == "*" else 0

    for i in range(left + 1, right + 1):
        has_top = top[i] == "*"
        has_bottom = bottom[i] == "*"

        next_top = min(
            top_cost + 1 + (1 if has_bottom else 0),
            bottom_cost + 1 + (0 if has_bottom else 1),
        )
        next_bottom = min(
            bottom_cost + 1 + (1 if has_top else 0),
            top_cost + 1 + (0 if has_top else 1),
        )

        top_cost, bottom_cost = next_top, next_bottom

    return top_cost if top_cost < bottom_cost else bottom_cost

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    values = []
    p = 1
    for _ in range(t):
        n = int(data[p])
        top = data[p + 1]
        bottom = data[p + 2]
        p += 3
        values.append(str(solve_case(n, top, bottom)))
    sys.stdout.write("\n".join(values))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
