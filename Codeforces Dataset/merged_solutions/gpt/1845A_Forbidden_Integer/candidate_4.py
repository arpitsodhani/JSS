import sys

# CLAUSE: analyze_available_generators
def analyze_available_generators(n, k, x):
    can_take = {v for v in (1, 2, 3) if v <= k and v != x}
    can_single = n in can_take or (3 < n <= k and n != x)
    return can_take, can_single

# CLAUSE: decide_constructive_strategy
def decide_constructive_strategy(n, k, x, can_take, can_single):
    if 1 in can_take:
        return ("unit", n)
    if 2 in can_take and n % 2 == 0:
        return ("pair", n // 2)
    if 3 in can_take and n % 2 == 1:
        return ("odd", 1 + (n - 3) // 2)
    return ("reject", 0)

# CLAUSE: build_unit_based_sum
def build_unit_based_sum(count):
    return [1 for _ in range(count)]

# CLAUSE: build_pair_based_sum
def build_pair_based_sum(count):
    return [2 for _ in range(count)]

# CLAUSE: validate_sum_representation
def validate_sum_representation(seq, n, k, x):
    if len(seq) == 0:
        return False
    total = 0
    for item in seq:
        total += item
        if not (1 <= item <= k) or item == x:
            return False
    return total == n

# CLAUSE: emit_answer_sequence
def emit_answer_sequence(seq, valid, writer):
    writer("YES\n" + str(len(seq)) + "\n" + " ".join(map(str, seq)) + "\n" if valid else "NO\n")

def solve_one(n, k, x):
    can_take, can_single = analyze_available_generators(n, k, x)
    kind, amount = decide_constructive_strategy(n, k, x, can_take, can_single)
    if kind == "unit":
        seq = build_unit_based_sum(amount)
    elif kind == "pair":
        seq = build_pair_based_sum(n)
    elif kind == "odd":
        seq = [3] + build_pair_based_sum(n - 3)
    else:
        seq = []
    return seq, validate_sum_representation(seq, n, k, x)

values = list(map(int, sys.stdin.buffer.read().split()))
out = []
pos = 1
for _ in range(values[0]):
    n, k, x = values[pos:pos + 3]
    pos += 3
    seq, valid = solve_one(n, k, x)
    emit_answer_sequence(seq, valid, out.append)
sys.stdout.write("".join(out))
