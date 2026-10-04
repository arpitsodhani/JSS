# CLAUSE: cap_power_counts
import sys

INF = 10**19

def prepare(limit):
    p = [0] * (limit + 1)
    p[0] = 1
    for i in range(1, limit + 1):
        p[i] = min(INF, p[i - 1] << 1)
    return p

# CLAUSE: validate_rank_feasibility
def has_answer(n, k, p):
    total = p[n - 1]
    return total >= k

# CLAUSE: model_reversed_blocks
def solve_case(n, k, p):
    pieces = []
    current = 1
    left = n

# CLAUSE: count_prefix_bucket
    def ways_after(take):
        rest = left - take
        return p[rest - 1] if rest > 0 else 1

# CLAUSE: select_next_block
    while left:
        take = 1
        while take < left and ways_after(take) < k:
            k -= ways_after(take)
            take += 1

# CLAUSE: emit_block_reversal
        pieces.append(" ".join(str(x) for x in range(current + take - 1, current - 1, -1)))

# CLAUSE: advance_unranking_state
        current += take
        left -= take
    return " ".join(piece for piece in pieces if piece)

def main():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    cases = []
    for i in range(t):
        cases.append((int(raw[2 * i + 1]), int(raw[2 * i + 2])))
    p = prepare(max(n for n, _ in cases))
    out = []
    for n, k in cases:
        out.append(solve_case(n, k, p) if has_answer(n, k, p) else "-1")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
