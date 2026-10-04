import sys

# CLAUSE: analyze_available_generators
def analyze_available_generators(n, k, x):
    return {
        "has_one": x != 1,
        "has_two": k > 1 and x != 2,
        "single": n <= k and n != x,
    }

# CLAUSE: decide_constructive_strategy
def decide_constructive_strategy(n, k, x, info):
    if info["has_one"]:
        return 1
    if info["has_two"] and n % 2 == 0:
        return 2
    if n % 2 == 1 and k >= 3 and x != 3:
        return 3
    return 0

# CLAUSE: build_unit_based_sum
def build_unit_based_sum(n):
    seq = []
    for _ in range(n):
        seq.append(1)
    return seq

# CLAUSE: build_pair_based_sum
def build_pair_based_sum(n):
    seq = []
    for _ in range(n // 2):
        seq.append(2)
    return seq

# CLAUSE: validate_sum_representation
def validate_sum_representation(seq, n, k, x):
    total = 0
    for value in seq:
        if value < 1 or value > k or value == x:
            return False
        total += value
    return total == n

# CLAUSE: emit_answer_sequence
def emit_answer_sequence(seq, valid):
    if not valid:
        return ["NO"]
    return ["YES", str(len(seq)), " ".join(str(v) for v in seq)]

def solve(n, k, x):
    info = analyze_available_generators(n, k, x)
    mode = decide_constructive_strategy(n, k, x, info)
    if mode == 1:
        seq = build_unit_based_sum(n)
    elif mode == 2:
        seq = build_pair_based_sum(n)
    elif mode == 3:
        seq = [3]
        seq.extend(build_pair_based_sum(n - 3))
    else:
        seq = []
    return emit_answer_sequence(seq, validate_sum_representation(seq, n, k, x))

tokens = list(map(int, sys.stdin.buffer.read().split()))
t = tokens[0]
lines = []
idx = 1
for _ in range(t):
    lines.extend(solve(tokens[idx], tokens[idx + 1], tokens[idx + 2]))
    idx += 3
sys.stdout.write("\n".join(lines))
