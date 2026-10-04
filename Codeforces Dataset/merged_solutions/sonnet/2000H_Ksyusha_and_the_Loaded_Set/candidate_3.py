# CLAUSE: setup_environment
import sys
import heapq

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.buffer.read().split()
    at = 0
    tests = int(tokens[at])
    at += 1
    output = []
    infinity = 10 ** 30

    for _ in range(tests):
        n = int(tokens[at])
        m = int(tokens[at + 1])
        at += 2

        starts = [int(tokens[at + i]) for i in range(n)]
        at += n

        queries = []
        universe = set(starts)
        universe.add(0)

        for _ in range(m):
            op = tokens[at]
            val = int(tokens[at + 1])
            at += 2
            queries.append((op, val))
            if op != b'?':
                universe.add(val)

        nums = sorted(universe)
        rank = {num: i for i, num in enumerate(nums)}
        count = len(nums)

        prev_node = [-1] * count
        next_node = [-1] * count
        used = [False] * count
        best = []

        def gap_size(a, b):
            if b < 0:
                return infinity
            return nums[b] - nums[a] - 1

        def offer(a, b):
            length = gap_size(a, b)
            if length:
                heapq.heappush(best, (-length, a, b))

        nodes = [rank[x] for x in sorted(set(starts))]
        nodes.insert(0, rank[0])

        for i, node in enumerate(nodes):
            used[node] = True
            if i:
                prev_node[node] = nodes[i - 1]
                next_node[nodes[i - 1]] = node

        for node in nodes:
            offer(node, next_node[node])

        for op, val in queries:
            if op == b'+':
                node = rank[val]
                if used[node]:
                    continue
                before = node - 1
                while not used[before]:
                    before -= 1
                after = next_node[before]
                used[node] = True
                prev_node[node] = before
                next_node[node] = after
                next_node[before] = node
                if after >= 0:
                    prev_node[after] = node
                offer(before, node)
                offer(node, after)
            elif op == b'-':
                node = rank[val]
                if not used[node]:
                    continue
                before = prev_node[node]
                after = next_node[node]
                used[node] = False
                next_node[before] = after
                if after >= 0:
                    prev_node[after] = before
                offer(before, after)
            else:
                while best:
                    neg_len, a, b = best[0]
                    if used[a] and next_node[a] == b and gap_size(a, b) == -neg_len:
                        break
                    heapq.heappop(best)
                if best and -best[0][0] >= val:
                    output.append(str(nums[best[0][1]] + 1))
                else:
                    output.append(str(nums[0] + 1))

    sys.stdout.write("\n".join(output))

# CLAUSE: finish_program
main()
