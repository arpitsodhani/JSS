# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    n, w, m = data

    if m > n and n % (m - n) != 0:
        print("NO")
    else:
        print("YES")
        for i in range(m):
            left_c = i * n
            right_c = (i + 1) * n
            parts = []
            for j in range(n):
                left_b = j * m
                right_b = (j + 1) * m
                x = min(right_c, right_b) - max(left_c, left_b)
                if x > 0:
                    parts.append(f"{j + 1} {x * w / m:.6f}")
            print(" ".join(parts))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
