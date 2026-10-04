import sys

# CLAUSE: normalize_parameters
def normalize_parameters(raw):
    values = [int(x) for x in raw.split()]
    return values[0], values[1], values[2], values[3], values[4:4 + values[0]]

# CLAUSE: initialize_exact_state
def initialize_exact_state(line_limit, bug_limit):
    table = []
    for line_count in range(line_limit + 1):
        row = [0] * (bug_limit + 1)
        table.append(row)
    table[0][0] = 1
    return table

# CLAUSE: process_programmer_type
def process_programmer_type(table, programmers, line_limit, bug_limit, modulus):
    for programmer_bug_rate in programmers:
        extend_same_programmer_usage(table, programmer_bug_rate, line_limit, bug_limit, modulus)

# CLAUSE: extend_same_programmer_usage
def extend_same_programmer_usage(table, programmer_bug_rate, line_limit, bug_limit, modulus):
    for line_count in range(1, line_limit + 1):
        previous_line = table[line_count - 1]
        current_line = table[line_count]
        for bug_count in range(programmer_bug_rate, bug_limit + 1):
            incoming = previous_line[bug_count - programmer_bug_rate]
            if incoming:
                current_line[bug_count] = accumulate_modulo_counts(current_line[bug_count], incoming, modulus)

# CLAUSE: accumulate_modulo_counts
def accumulate_modulo_counts(left, right, modulus):
    total = left + right
    if total >= modulus:
        total %= modulus
    return total

# CLAUSE: prune_unreachable_bug_states
def prune_unreachable_bug_states(table, line_limit, bug_limit):
    return table[:line_limit + 1], bug_limit

# CLAUSE: aggregate_good_plans
n, m, b, mod, rates = normalize_parameters(sys.stdin.buffer.read())
dp = initialize_exact_state(m, b)
dp, b = prune_unreachable_bug_states(dp, m, b)
process_programmer_type(dp, rates, m, b, mod)
print(sum(dp[m]) % mod)
