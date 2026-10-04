# CLAUSE: setup_environment
import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]

# CLAUSE: solve_logic
    order = sorted(range(n), key=lambda i: (a[i], i))
    rank_at_pos = [0] * n
    for rank, pos in enumerate(order):
        rank_at_pos[pos] = rank

    pos_of_rank = [0] * n
    for pos, rank in enumerate(rank_at_pos):
        pos_of_rank[rank] = pos

    queue = deque()
    for rank in range(n - 1):
        if pos_of_rank[rank] > pos_of_rank[rank + 1]:
            queue.append(rank)

    ans = []
    while queue:
        rank = queue.popleft()
        if rank < 0 or rank + 1 >= n:
            continue
        left_pos = pos_of_rank[rank]
        right_pos = pos_of_rank[rank + 1]
        if left_pos < right_pos:
            continue

        u, v = right_pos, left_pos
        ans.append((u + 1, v + 1))

        rank_at_pos[left_pos], rank_at_pos[right_pos] = rank_at_pos[right_pos], rank_at_pos[left_pos]
        pos_of_rank[rank], pos_of_rank[rank + 1] = right_pos, left_pos

        for nxt in (rank - 1, rank, rank + 1):
            if 0 <= nxt < n - 1 and pos_of_rank[nxt] > pos_of_rank[nxt + 1]:
                queue.append(nxt)

# CLAUSE: finish_program
    result = [str(len(ans))]
    result += [str(u) + " " + str(v) for u, v in ans]
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
