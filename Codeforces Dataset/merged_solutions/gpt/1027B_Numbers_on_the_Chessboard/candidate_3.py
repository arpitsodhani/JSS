# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    n, q = data[0], data[1]

    white_total = (n * n + 1) // 2
    ans = []
    idx = 2

    for _ in range(q):
        x, y = data[idx], data[idx + 1]
        idx += 2

        if (x + y) % 2 == 0:
            if n % 2 == 1:
                k = ((x - 1) * n + y + 1) // 2
            else:
                k = (x - 1) * (n // 2)
                k += (y + 1) // 2 if x % 2 == 1 else y // 2
            ans.append(str(k))
        else:
            if n % 2 == 1:
                k = ((x - 1) * n + y) // 2
            else:
                k = (x - 1) * (n // 2)
                k += y // 2 if x % 2 == 1 else (y + 1) // 2
            ans.append(str(white_total + k))

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
