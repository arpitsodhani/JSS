# CLAUSE: cap_power_counts
import sys

LIMIT = 10**18 + 5

def build_powers(max_n):
    powers = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        powers[i] = min(LIMIT, powers[i - 1] * 2)
    return powers

# CLAUSE: validate_rank_feasibility
def feasible(n, k, powers):
    return k <= powers[n - 1]

# CLAUSE: model_reversed_blocks
def construct(n, k, powers):
    ans = []
    start = 1
    remaining = n

# CLAUSE: count_prefix_bucket
    def bucket_size(rem, block_len):
        tail = rem - block_len
        if tail <= 0:
            return 1
        return powers[tail - 1]

# CLAUSE: select_next_block
    while remaining:
        chosen = 1
        for length in range(1, remaining + 1):
            ways = bucket_size(remaining, length)
            if k > ways:
                k -= ways
            else:
                chosen = length
                break

# CLAUSE: emit_block_reversal
        for value in range(start + chosen - 1, start - 1, -1):
            ans.append(value)

# CLAUSE: advance_unranking_state
        start += chosen
        remaining -= chosen
    return ans

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pairs = [(data[i], data[i + 1]) for i in range(1, len(data), 2)]
    powers = build_powers(max(n for n, _ in pairs))
    out = []
    for n, k in pairs[:t]:
        if not feasible(n, k, powers):
            out.append("-1")
        else:
            out.append(" ".join(map(str, construct(n, k, powers))))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
