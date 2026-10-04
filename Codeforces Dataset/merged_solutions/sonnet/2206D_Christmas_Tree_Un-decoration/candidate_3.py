# CLAUSE: setup_environment
import sys
import heapq

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    at = 0
    tests = nums[at]
    at += 1
    answers = []

    for _ in range(tests):
        n = nums[at]
        q = nums[at + 1]
        at += 2

        par = [0] * (n + 1)
        ch = [[] for _ in range(n + 1)]
        for node in range(2, n + 1):
            p = nums[at]
            at += 1
            par[node] = p
            ch[p].append(node)

        val = [0] * (n + 1)
        for node in range(1, n + 1):
            val[node] = nums[at]
            at += 1

        seq = []
        stack = [1]
        while stack:
            node = stack.pop()
            seq.append(node)
            stack.extend(ch[node])

        need = [0] * (n + 1)
        bonus = [0] * (n + 1)
        for node in seq[::-1]:
            total = 0
            for kid in ch[node]:
                total += need[kid]
            if val[node] >= total:
                need[node] = val[node]
                bonus[node] = val[node] - total
            else:
                need[node] = total

        tin = [0] * (n + 1)
        tout = [0] * (n + 1)
        clock = 0
        stack = [(1, 0)]
        while stack:
            node, seen = stack.pop()
            if seen:
                tout[node] = clock
            else:
                clock += 1
                tin[node] = clock
                stack.append((node, 1))
                for kid in ch[node][::-1]:
                    stack.append((kid, 0))

        vertex = [0] * (n + 1)
        heap = []
        for node in range(1, n + 1):
            vertex[tin[node]] = node
            if bonus[node]:
                heapq.heappush(heap, -tin[node])

        root_answer = need[1]
        answers.append(str(root_answer))

        for _ in range(q):
            node = nums[at]
            x = nums[at + 1]
            at += 2

            old_bonus = bonus[node]
            unchanged_part = val[node] - old_bonus
            new_bonus = x - unchanged_part
            if new_bonus < 0:
                new_bonus = 0
            val[node] = x

            if new_bonus != old_bonus:
                bonus[node] = new_bonus
                if old_bonus == 0 and new_bonus > 0:
                    heapq.heappush(heap, -tin[node])

                diff = new_bonus - old_bonus
                root_answer += diff

                while diff > 0:
                    while heap:
                        top_time = -heap[0]
                        top_node = vertex[top_time]
                        if bonus[top_node] and top_time <= tin[node]:
                            break
                        heapq.heappop(heap)
                    if not heap:
                        break

                    top_time = -heap[0]
                    top_node = vertex[top_time]
                    if tout[top_node] < tin[node]:
                        break

                    use = bonus[top_node] if bonus[top_node] < diff else diff
                    bonus[top_node] -= use
                    root_answer -= use
                    diff -= use
                    if bonus[top_node] == 0:
                        heapq.heappop(heap)

            answers.append(str(root_answer))

    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
