# CLAUSE: cap_power_counts
import sys

BOUND = 10**18 + 100

def capped_counts(n):
    counts = [1] * max(1, n)
    value = 1
    for i in range(1, n):
        value = min(BOUND, value * 2)
        counts[i] = value
    return counts

# CLAUSE: validate_rank_feasibility
def ok_rank(n, k, counts):
    return k <= counts[n - 1]

# CLAUSE: model_reversed_blocks
def produce(n, k, counts):
    ans = []
    next_value = 1
    remaining = n

# CLAUSE: count_prefix_bucket
    def bucket(block_len):
        suffix_len = remaining - block_len
        return 1 if suffix_len < 1 else counts[suffix_len - 1]

# CLAUSE: select_next_block
    while remaining > 0:
        options = (bucket(length) for length in range(1, remaining + 1))
        chosen = 1
        for chosen, amount in enumerate(options, 1):
            if k <= amount:
                break
            k -= amount

# CLAUSE: emit_block_reversal
        end_value = next_value + chosen - 1
        ans.extend(reversed(range(next_value, end_value + 1)))

# CLAUSE: advance_unranking_state
        next_value = end_value + 1
        remaining -= chosen
    return ans

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = [(data[i], data[i + 1]) for i in range(1, 2 * t + 1, 2)]
    counts = capped_counts(max(n for n, _ in cases))
    lines = []
    for n, k in cases:
        if ok_rank(n, k, counts):
            lines.append(" ".join(map(str, produce(n, k, counts))))
        else:
            lines.append("-1")
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
