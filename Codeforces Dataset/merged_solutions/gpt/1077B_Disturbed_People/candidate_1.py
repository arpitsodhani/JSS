# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:1 + n]

    ans = 0
    for i in range(1, n - 1):
        if a[i] == 0 and a[i - 1] == 1 and a[i + 1] == 1:
            ans += 1
            a[i + 1] = 0

    print(ans)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
