import sys

# CLAUSE: normalize_parameters
def normalize_parameters():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m, b, mod = data[:4]
    rates = data[4:4 + n]
    return n, m, b, mod, rates

# CLAUSE: initialize_exact_state
def initialize_exact_state(m, b):
    dp = [[0] * (b + 1) for _ in range(m + 1)]
    dp[0][0] = 1
    return dp

# CLAUSE: process_programmer_type
def process_programmer_type(dp, rates, m, b, mod):
    for bugs_per_line in rates:
        extend_same_programmer_usage(dp, bugs_per_line, m, b, mod)
    return dp

# CLAUSE: extend_same_programmer_usage
def extend_same_programmer_usage(dp, bugs_per_line, m, b, mod):
    for lines in range(1, m + 1):
        for bugs in prune_unreachable_bug_states(bugs_per_line, b):
            dp[lines][bugs] = accumulate_modulo_counts(
                dp[lines][bugs],
                dp[lines - 1][bugs - bugs_per_line],
                mod
            )

# CLAUSE: accumulate_modulo_counts
def accumulate_modulo_counts(current, added, mod):
    return (current + added) % mod

# CLAUSE: prune_unreachable_bug_states
def prune_unreachable_bug_states(cost, b):
    return range(cost, b + 1)

# CLAUSE: aggregate_good_plans
def aggregate_good_plans(dp, m, b, mod):
    return sum(dp[m][bugs] for bugs in range(b + 1)) % mod

n, m, b, mod, rates = normalize_parameters()
dp = initialize_exact_state(m, b)
process_programmer_type(dp, rates, m, b, mod)
print(aggregate_good_plans(dp, m, b, mod))
