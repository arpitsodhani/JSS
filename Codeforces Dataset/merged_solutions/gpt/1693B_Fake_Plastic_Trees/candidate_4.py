import sys

sys.setrecursionlimit(2_000_000)

def solve_case(n, parents, bounds):
    # CLAUSE: build_child_adjacency
    g = [[] for _ in range(n + 1)]
    for idx, p in enumerate(parents, 2):
        g[p].append(idx)

    answer = 0

    # CLAUSE: traverse_subtree_postorder
    def visit(v):
        nonlocal answer

        # CLAUSE: aggregate_child_capacity
        gathered = sum(visit(u) for u in g[v])

        lo, hi = bounds[v]

        # CLAUSE: enforce_vertex_lower_bound
        if gathered < lo:
            answer += 1

            # CLAUSE: cap_vertex_contribution
            return hi

        # CLAUSE: cap_vertex_contribution
        return min(gathered, hi)

    # CLAUSE: count_required_operations
    visit(1)
    return answer

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    at = 0
    q = nums[at]
    at += 1
    ans = []

    for _ in range(q):
        n = nums[at]
        at += 1
        parents = nums[at:at + n - 1]
        at += n - 1

        bounds = [None] * (n + 1)
        for v in range(1, n + 1):
            bounds[v] = (nums[at], nums[at + 1])
            at += 2

        ans.append(str(solve_case(n, parents, bounds)))

    sys.stdout.write("\n".join(ans))

main()
