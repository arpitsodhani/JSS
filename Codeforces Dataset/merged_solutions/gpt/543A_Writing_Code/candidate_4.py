import sys

# CLAUSE: normalize_parameters
def normalize_parameters():
    stream = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(stream)
    m = next(stream)
    b = next(stream)
    mod = next(stream)
    bugs = [next(stream) for _ in range(n)]
    return m, b, mod, bugs

# CLAUSE: initialize_exact_state
def initialize_exact_state(m, b):
    state = {(0, 0): 1}
    return state

# CLAUSE: process_programmer_type
def process_programmer_type(state, rates, m, b, mod):
    for rate in rates:
        extend_same_programmer_usage(state, rate, m, b, mod)
    return state

# CLAUSE: extend_same_programmer_usage
def extend_same_programmer_usage(state, rate, m, b, mod):
    for lines in range(1, m + 1):
        for bugs in range(rate, b + 1):
            previous = state.get((lines - 1, bugs - rate), 0)
            if previous:
                key = (lines, bugs)
                state[key] = accumulate_modulo_counts(state.get(key, 0), previous, mod)

# CLAUSE: accumulate_modulo_counts
def accumulate_modulo_counts(current, extra, mod):
    return (current + extra) % mod

# CLAUSE: prune_unreachable_bug_states
def prune_unreachable_bug_states(state, m, b):
    return {
        key: value
        for key, value in state.items()
        if key[0] <= m and key[1] <= b
    }

# CLAUSE: aggregate_good_plans
m, b, mod, rates = normalize_parameters()
dp = initialize_exact_state(m, b)
dp = process_programmer_type(dp, rates, m, b, mod)
dp = prune_unreachable_bug_states(dp, m, b)
print(sum(dp.get((m, bugs), 0) for bugs in range(b + 1)) % mod)
