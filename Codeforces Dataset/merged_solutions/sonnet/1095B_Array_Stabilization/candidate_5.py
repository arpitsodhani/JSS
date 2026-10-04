# CLAUSE: setup_environment
n = int(input())
arr = list(map(int, input().split()))

# CLAUSE: solve_logic
arr.sort()
def instability_after_drop(index):
    if index == 0:
        return arr[-1] - arr[1]
    return arr[-2] - arr[0]

ans = 0
if n > 2:
    ans = min(instability_after_drop(0), instability_after_drop(n - 1))

# CLAUSE: finish_program
print(ans)
