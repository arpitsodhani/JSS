import sys

# CLAUSE: analyze_available_generators
def analyze_available_generators(n, k, x):
    one_available = 1 <= k and x != 1
    two_available = 2 <= k and x != 2
    single_available = n <= k and n != x
    return (one_available, two_available, single_available)

# CLAUSE: decide_constructive_strategy
def decide_constructive_strategy(n, k, x, analysis):
    one_available, two_available, single_available = analysis
    if one_available:
        return 0
    if two_available and n % 2 == 0:
        return 1
    if n % 2 and k >= 3 and x != 3:
        return 2
    return -1

# CLAUSE: build_unit_based_sum
def build_unit_based_sum(n):
    seq = [0] * n
    for i in range(n):
        seq[i] = 1
    return seq

# CLAUSE: build_pair_based_sum
def build_pair_based_sum(n):
    count = n // 2
    seq = [0] * count
    for i in range(count):
        seq[i] = 2
    return seq

# CLAUSE: validate_sum_representation
def validate_sum_representation(seq, n, k, x):
    return len(seq) > 0 and sum(seq) == n and all(1 <= a <= k and a != x for a in seq)

# CLAUSE: emit_answer_sequence
def emit_answer_sequence(seq, valid):
    if valid:
        return f"YES\n{len(seq)}\n{' '.join(map(str, seq))}"
    return "NO"

def make_answer(n, k, x):
    analysis = analyze_available_generators(n, k, x)
    case = decide_constructive_strategy(n, k, x, analysis)
    builders = {
        0: lambda: build_unit_based_sum(n),
        1: lambda: build_pair_based_sum(n),
        2: lambda: [3] + build_pair_based_sum(n - 3),
    }
    seq = builders[case]() if case in builders else []
    return emit_answer_sequence(seq, validate_sum_representation(seq, n, k, x))

nums = list(map(int, sys.stdin.buffer.read().split()))
answers = []
offset = 1
for _ in range(nums[0]):
    answers.append(make_answer(nums[offset], nums[offset + 1], nums[offset + 2]))
    offset += 3
print("\n".join(answers))
