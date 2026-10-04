# CLAUSE: cap_power_counts
import sys

CAP = 4 * 10**18

def capped_power(exp):
    if exp >= 62:
        return CAP
    return 1 << exp

# CLAUSE: validate_rank_feasibility
def rank_is_valid(n, k):
    return k <= capped_power(n - 1)

# CLAUSE: model_reversed_blocks
def kth_permutation(n, k):
    result = []
    low = 1

# CLAUSE: count_prefix_bucket
    def count_with_first_block(length, rem):
        after = rem - length
        return 1 if after == 0 else capped_power(after - 1)

# CLAUSE: select_next_block
    while low <= n:
        rem = n - low + 1
        length = 1
        while length <= rem:
            cnt = count_with_first_block(length, rem)
            if cnt >= k:
                break
            k -= cnt
            length += 1

# CLAUSE: emit_block_reversal
        result.extend(range(low + length - 1, low - 1, -1))

# CLAUSE: advance_unranking_state
        low += length
    return result

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    t = values[0]
    answer_lines = []
    pos = 1
    for _ in range(t):
        n, k = values[pos], values[pos + 1]
        pos += 2
        if not rank_is_valid(n, k):
            answer_lines.append("-1")
            continue
        answer_lines.append(" ".join(str(x) for x in kth_permutation(n, k)))
    print("\n".join(answer_lines))

if __name__ == "__main__":
    main()
