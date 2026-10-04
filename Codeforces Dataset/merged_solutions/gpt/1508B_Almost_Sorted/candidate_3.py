# CLAUSE: cap_power_counts
import sys

MAX_K = 10**18

def make_count_table(size):
    table = [1]
    for _ in range(size):
        table.append(min(MAX_K + 1, table[-1] + table[-1]))
    return table

# CLAUSE: validate_rank_feasibility
def impossible(n, k, table):
    return table[n - 1] < k

# CLAUSE: model_reversed_blocks
def unrank_blocks(n, k, table):
    output = []
    first_unused = 1
    rem = n

# CLAUSE: count_prefix_bucket
    def suffix_count(block_end):
        left = rem - block_end
        return 1 if left == 0 else table[left - 1]

# CLAUSE: select_next_block
    while rem > 0:
        block_len = 0
        skipped = 0
        for candidate in range(1, rem + 1):
            ways = suffix_count(candidate)
            if skipped + ways >= k:
                block_len = candidate
                k -= skipped
                break
            skipped += ways

# CLAUSE: emit_block_reversal
        block = list(range(first_unused, first_unused + block_len))
        output += block[::-1]

# CLAUSE: advance_unranking_state
        first_unused += block_len
        rem -= block_len
    return output

def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    tests = nums[0]
    cases = []
    idx = 1
    for _ in range(tests):
        cases.append((nums[idx], nums[idx + 1]))
        idx += 2
    table = make_count_table(max(n for n, _ in cases))
    lines = []
    for n, k in cases:
        if impossible(n, k, table):
            lines.append("-1")
        else:
            lines.append(" ".join(map(str, unrank_blocks(n, k, table))))
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
