# Clause setup_environment [Confidence: 0.60]
import sys

MOD = 1000000007


# Clause solve_logic [Confidence: 1.00]
def build_tree(n, nums):
    adjacency = [[] for _ in range(n)]
    for i in range(1, len(nums), 3):
        x, y, z = nums[i], nums[i + 1], nums[i + 2] % MOD
        adjacency[x].append((y, z))
        adjacency[y].append((x, z))
    return adjacency

def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    if not nums:
        return

    n = nums[0]
    adjacency = build_tree(n, nums)

    parent = [-2] * n
    incoming = [0] * n
    parent[0] = -1
    stack = [0]
    traversal = []

    while stack:
        cur = stack.pop()
        traversal.append(cur)
        for nxt, dist in adjacency[cur]:
            if parent[nxt] == -2:
                parent[nxt] = cur
                incoming[nxt] = dist
                stack.append(nxt)

    alpha = [0] * n
    beta = [0] * n

    for cur in reversed(traversal):
        if cur == 0 or len(adjacency[cur]) == 1:
            continue
        total_alpha = 0
        total_beta = incoming[cur]
        for nxt, dist in adjacency[cur]:
            if parent[nxt] == cur:
                total_alpha += alpha[nxt]
                total_beta += dist + beta[nxt]
        total_alpha %= MOD
        total_beta %= MOD
        divisor = (len(adjacency[cur]) - total_alpha) % MOD
        alpha[cur] = pow(divisor, MOD - 2, MOD)
        beta[cur] = total_beta * alpha[cur] % MOD

    top_alpha = 0
    top_beta = 0
    for nxt, dist in adjacency[0]:
        top_alpha = (top_alpha + alpha[nxt]) % MOD
        top_beta = (top_beta + dist + beta[nxt]) % MOD

    print(top_beta * pow((len(adjacency[0]) - top_alpha) % MOD, MOD - 2, MOD) % MOD)


# Clause finish_program [Confidence: 0.40]
main()


