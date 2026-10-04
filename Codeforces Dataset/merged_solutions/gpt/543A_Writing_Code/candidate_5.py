import sys

# CLAUSE: normalize_parameters
def normalize_parameters():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    b = int(data[2])
    mod = int(data[3])
    bugs = list(map(int, data[4:4 + n]))
    return n, m, b, mod, bugs

# CLAUSE: initialize_exact_state
def initialize_exact_state(m, b):
    return [[1 if line == 0 and bug == 0 else 0 for bug in range(b + 1)] for line in range(m + 1)]

# CLAUSE: process_programmer_type
def process_programmer_type(dp, bugs_by_programmer, m, b, mod):
    for cost in bugs_by_programmer:
        extend_same_programmer_usage(dp, cost, m, b, mod)

# CLAUSE: extend_same_programmer_usage
def extend_same_programmer_usage(dp, cost, m, b, mod):
    for bug_total in range(cost, b + 1):
        for line_total in range(1, m + 1):
            add = dp[line_total - 1][bug_total - cost]
            if add:
                dp[line_total][bug_total] = accumulate_modulo_counts(dp[line_total][bug_total], add, mod)

# CLAUSE: accumulate_modulo_counts
def accumulate_modulo_counts(base, inc, mod):
    base += inc
    base %= mod
    return base

# CLAUSE: prune_unreachable_bug_states
def prune_unreachable_bug_states(m, b):
    return range(m + 1), range(b + 1)

# CLAUSE: aggregate_good_plans
n, m, b, mod, bugs_by_programmer = normalize_parameters()
dp = initialize_exact_state(m, b)
line_range, bug_range = prune_unreachable_bug_states(m, b)
process_programmer_type(dp, bugs_by_programmer, m, b, mod)
result = 0
for bug_total in bug_range:
    result = accumulate_modulo_counts(result, dp[m][bug_total], mod)
print(result)
