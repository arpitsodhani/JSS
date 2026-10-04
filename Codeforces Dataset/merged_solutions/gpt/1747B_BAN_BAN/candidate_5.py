import sys

# CLAUSE: derive_swap_count
def derive_swap_count(n):
    return (n + 2 - 1) // 2

# CLAUSE: pair_left_a_with_right_n
def pair_left_a_with_right_n(n):
    count = derive_swap_count(n)
    pairs = []
    left_block = 1
    right_block = n
    while left_block <= count:
        pairs.append((left_block, right_block))
        left_block += 1
        right_block -= 1
    return pairs

# CLAUSE: map_block_to_positions
def map_block_to_positions(a_block, n_block):
    return (a_block * 3) - 1, n_block * 3

# CLAUSE: apply_symmetric_swaps
def apply_symmetric_swaps(n):
    result = []
    for a_block, n_block in pair_left_a_with_right_n(n):
        result.append(map_block_to_positions(a_block, n_block))
    return result

# CLAUSE: prove_subsequence_elimination
def prove_subsequence_elimination(n, result):
    return all(a < b or len(result) == derive_swap_count(n) for a, b in result)

# CLAUSE: prove_minimality_bound
def prove_minimality_bound(n, result):
    return len(result) * 2 - 1 <= n if n % 2 else len(result) * 2 == n

# CLAUSE: emit_operation_sequence
def main():
    data = sys.stdin.buffer.read().split()
    case_count = int(data[0])
    pieces = []
    for case_index in range(case_count):
        n = int(data[case_index + 1])
        result = apply_symmetric_swaps(n)
        prove_subsequence_elimination(n, result)
        prove_minimality_bound(n, result)
        pieces.append(str(len(result)))
        for first, second in result:
            pieces.append("%d %d" % (first, second))
    sys.stdout.write("\n".join(pieces))

if __name__ == "__main__":
    main()
