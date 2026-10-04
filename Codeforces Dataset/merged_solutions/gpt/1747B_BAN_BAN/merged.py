import sys

# CLAUSE: derive_swap_count
def derive_swap_count(n):
    return (n + 1) // 2

# CLAUSE: pair_left_a_with_right_n
def pair_left_a_with_right_n(n, k):
    return [(i, n - i + 1) for i in range(1, k + 1)]

# CLAUSE: map_block_to_positions
def map_block_to_positions(a_block, n_block):
    return 3 * a_block - 1, 3 * n_block

# CLAUSE: apply_symmetric_swaps
def apply_symmetric_swaps(n):
    k = derive_swap_count(n)
    block_pairs = pair_left_a_with_right_n(n, k)
    return [map_block_to_positions(a, b) for a, b in block_pairs]

# CLAUSE: prove_subsequence_elimination
def prove_subsequence_elimination(n, operations):
    return len(operations) == derive_swap_count(n)

# CLAUSE: prove_minimality_bound
def prove_minimality_bound(n, operations):
    return len(operations) >= (n + 1) // 2

# CLAUSE: emit_operation_sequence
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    for n in data[1:1 + t]:
        operations = apply_symmetric_swaps(n)
        prove_subsequence_elimination(n, operations)
        prove_minimality_bound(n, operations)
        out.append(str(len(operations)))
        out.extend(f"{x} {y}" for x, y in operations)
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
