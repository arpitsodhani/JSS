# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = sys.stdin.read().split()
    if not data:
        sys.exit()

    n = int(data[0])
    male = [0] * 367
    female = [0] * 367

    idx = 1
    for _ in range(n):
        g = data[idx]
        a = int(data[idx + 1])
        b = int(data[idx + 2])
        idx += 3
        arr = male if g == 'M' else female
        for day in range(a, b + 1):
            arr[day] += 1

    ans = 0
    for day in range(1, 367):
        ans = max(ans, 2 * min(male[day], female[day]))

    print(ans)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
