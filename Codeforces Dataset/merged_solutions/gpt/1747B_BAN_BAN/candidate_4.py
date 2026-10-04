import sys

# CLAUSE: derive_swap_count
def derive_swap_count(n):
    return (n >> 1) + (n & 1)

# CLAUSE: pair_left_a_with_right_n
def pair_left_a_with_right_n(n):
    k = derive_swap_count(n)
    left = list(range(1, k + 1))
    right = list(range(n, n - k, -1))
    return zip(left, right)

# CLAUSE: map_block_to_positions
def map_block_to_positions(a_block, n_block):
    positions = (3 * a_block - 1, 3 * n_block)
    return positions

# CLAUSE: apply_symmetric_swaps
def apply_symmetric_swaps(n):
    return [map_block_to_positions(a_block, n_block)
            for a_block, n_block in pair_left_a_with_right_n(n)]

# CLAUSE: prove_subsequence_elimination
def prove_subsequence_elimination(n, swaps):
    moved_a_blocks = len(swaps)
    return moved_a_blocks >= n - moved_a_blocks

# CLAUSE: prove_minimality_bound
def prove_minimality_bound(n, swaps):
    smaller = len(swaps) - 1
    return smaller < derive_swap_count(n)

# CLAUSE: emit_operation_sequence
def main():
    raw = sys.stdin.buffer.read().split()
    total = int(raw[0])
    lines = []
    for idx in range(total):
        n = int(raw[idx + 1])
        swaps = apply_symmetric_swaps(n)
        prove_subsequence_elimination(n, swaps)
        prove_minimality_bound(n, swaps)
        lines.append(str(len(swaps)))
        lines.extend(map(lambda p: f"{p[0]} {p[1]}", swaps))
    sys.stdout.write("\n".join(lines))

main()
