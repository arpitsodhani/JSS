import sys

# CLAUSE: analyze_available_generators
def analyze_available_generators(n, k, x):
    usable = [False, x != 1, k >= 2 and x != 2, k >= 3 and x != 3]
    direct = n <= k and n != x
    return usable, direct

# CLAUSE: decide_constructive_strategy
def decide_constructive_strategy(n, k, x, usable, direct):
    if usable[1]:
        return "ones"
    if usable[2] and n % 2 == 0:
        return "evens"
    if usable[3] and n % 2 == 1:
        return "three"
    return "bad"

# CLAUSE: build_unit_based_sum
def build_unit_based_sum(n):
    return list(1 for _ in range(n))

# CLAUSE: build_pair_based_sum
def build_pair_based_sum(n):
    return list(2 for _ in range(n // 2))

# CLAUSE: validate_sum_representation
def validate_sum_representation(seq, n, k, x):
    total = sum(seq)
    limits_ok = min(seq, default=0) >= 1 and max(seq, default=k + 1) <= k
    forbidden_ok = x not in seq
    return bool(seq) and total == n and limits_ok and forbidden_ok

# CLAUSE: emit_answer_sequence
def emit_answer_sequence(seq, valid):
    if valid:
        print("YES")
        print(len(seq))
        print(*seq)
    else:
        print("NO")

def process(n, k, x):
    usable, direct = analyze_available_generators(n, k, x)
    choice = decide_constructive_strategy(n, k, x, usable, direct)
    seq = []
    if choice == "ones":
        seq = build_unit_based_sum(n)
    if choice == "evens":
        seq = build_pair_based_sum(n)
    if choice == "three":
        seq = [3] + build_pair_based_sum(n - 3)
    emit_answer_sequence(seq, validate_sum_representation(seq, n, k, x))

it = iter(map(int, sys.stdin.buffer.read().split()))
t = next(it)
for _ in range(t):
    process(next(it), next(it), next(it))
