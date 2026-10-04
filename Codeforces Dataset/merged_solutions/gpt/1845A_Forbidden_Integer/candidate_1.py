import sys

# CLAUSE: analyze_available_generators
def analyze_available_generators(n, k, x):
    one_ok = x != 1
    two_ok = k >= 2 and x != 2
    direct_ok = 1 <= n <= k and n != x
    return one_ok, two_ok, direct_ok

# CLAUSE: decide_constructive_strategy
def decide_constructive_strategy(n, k, x, one_ok, two_ok, direct_ok):
    if one_ok:
        return "unit"
    if two_ok and n % 2 == 0:
        return "pair"
    if k >= 3 and x != 3 and n >= 3 and n % 2 == 1:
        return "odd"
    return "none"

# CLAUSE: build_unit_based_sum
def build_unit_based_sum(n):
    return [1] * n

# CLAUSE: build_pair_based_sum
def build_pair_based_sum(n):
    return [2] * (n // 2)

# CLAUSE: validate_sum_representation
def validate_sum_representation(seq, n, k, x):
    if not seq:
        return False
    if sum(seq) != n:
        return False
    return all(1 <= v <= k and v != x for v in seq)

# CLAUSE: emit_answer_sequence
def emit_answer_sequence(seq, ok, out):
    if not ok:
        out.append("NO")
    else:
        out.append("YES")
        out.append(str(len(seq)))
        out.append(" ".join(map(str, seq)))

def solve_case(n, k, x):
    one_ok, two_ok, direct_ok = analyze_available_generators(n, k, x)
    strategy = decide_constructive_strategy(n, k, x, one_ok, two_ok, direct_ok)
    if strategy == "unit":
        seq = build_unit_based_sum(n)
    elif strategy == "pair":
        seq = build_pair_based_sum(n)
    elif strategy == "odd":
        seq = [3] + build_pair_based_sum(n - 3)
    else:
        seq = []
    return seq, validate_sum_representation(seq, n, k, x)

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
ans = []
p = 1
for _ in range(t):
    n, k, x = data[p], data[p + 1], data[p + 2]
    p += 3
    seq, ok = solve_case(n, k, x)
    emit_answer_sequence(seq, ok, ans)
print("\n".join(ans))
