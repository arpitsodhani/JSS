import sys

# CLAUSE: normalize_parameters
tokens = list(map(int, sys.stdin.buffer.read().split()))
n = tokens[0]
m = tokens[1]
b = tokens[2]
mod = tokens[3]
a = tokens[4:4 + n]

# CLAUSE: initialize_exact_state
ways = [[0 for _ in range(b + 1)] for _ in range(m + 1)]
ways[0][0] = 1

# CLAUSE: process_programmer_type
for idx in range(n):
    bug_cost = a[idx]

    # CLAUSE: extend_same_programmer_usage
    for made_lines in range(m):
        source = ways[made_lines]
        target = ways[made_lines + 1]

        # CLAUSE: accumulate_modulo_counts
        for old_bugs, count in enumerate(source):

            # CLAUSE: prune_unreachable_bug_states
            new_bugs = old_bugs + bug_cost
            if count and new_bugs <= b:
                target[new_bugs] = (target[new_bugs] + count) % mod

# CLAUSE: aggregate_good_plans
answer = 0
for value in ways[m]:
    answer += value
    answer %= mod
print(answer)
