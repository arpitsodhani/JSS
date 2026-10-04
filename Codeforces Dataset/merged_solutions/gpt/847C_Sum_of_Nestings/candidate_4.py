# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    n, k = map(int, input().split())

    if k > n * (n - 1) // 2:
        print("Impossible")
    else:
        ans = []
        depth = 0
        for i in range(n):
            rem = n - i - 1
            d = min(depth, k)
            while d > 0 and k - d > rem * (rem - 1) // 2 + rem * d:
                d -= 1
            ans.append(')' * (depth - d))
            ans.append('(')
            k -= d
            depth = d + 1
        ans.append(')' * depth)
        print(''.join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
