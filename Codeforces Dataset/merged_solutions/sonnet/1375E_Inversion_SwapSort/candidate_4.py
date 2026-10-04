# CLAUSE: setup_environment
import sys

def build_ranks(a):
    n = len(a)
    rank_at_pos = [0] * n
    pos_of_rank = [0] * n
    for rank, pos in enumerate(sorted(range(n), key=lambda x: (a[x], x))):
        rank_at_pos[pos] = rank
        pos_of_rank[rank] = pos
    return rank_at_pos, pos_of_rank

def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    n = int(raw[0])
    a = list(map(int, raw[1:1 + n]))

# CLAUSE: solve_logic
    rank_at_pos, pos_of_rank = build_ranks(a)
    active = {r for r in range(n - 1) if pos_of_rank[r] > pos_of_rank[r + 1]}
    answer = []

    while active:
        r = active.pop()
        if pos_of_rank[r] <= pos_of_rank[r + 1]:
            continue

        p = pos_of_rank[r]
        q = pos_of_rank[r + 1]
        if p < q:
            u, v = p, q
        else:
            u, v = q, p
        answer.append((u + 1, v + 1))

        rank_at_pos[p], rank_at_pos[q] = rank_at_pos[q], rank_at_pos[p]
        pos_of_rank[r], pos_of_rank[r + 1] = q, p

        for x in range(r - 1, r + 2):
            if 0 <= x < n - 1 and pos_of_rank[x] > pos_of_rank[x + 1]:
                active.add(x)

# CLAUSE: finish_program
    sys.stdout.write(str(len(answer)))
    if answer:
        sys.stdout.write("\n")
        sys.stdout.write("\n".join("{} {}".format(u, v) for u, v in answer))

if __name__ == "__main__":
    main()
