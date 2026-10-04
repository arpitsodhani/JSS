# CLAUSE: setup_environment
import sys

MOD = 1000000007

# CLAUSE: solve_logic
def combine(state, child_state):
    zero, one = state
    child_zero, child_one = child_state
    total = (child_zero + child_one) % MOD
    return zero * total % MOD, (one * total + zero * child_one) % MOD

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    n = nums[0]
    parent_end = n
    colors = nums[parent_end:parent_end + n]
    children = [[] for _ in range(n)]

    for child, parent in enumerate(nums[1:parent_end], 1):
        children[parent].append(child)

    ways = [(0, 0)] * n
    for node in range(n - 1, -1, -1):
        state = (0, 1) if colors[node] else (1, 0)
        for child in children[node]:
            state = combine(state, ways[child])
        ways[node] = state

    sys.stdout.write(str(ways[0][1] % MOD))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
