import sys

# CLAUSE: derive_swap_count
def derive_swap_count(n):
    half, odd = divmod(n, 2)
    return half + odd

# CLAUSE: pair_left_a_with_right_n
def pair_left_a_with_right_n(n):
    count = derive_swap_count(n)
    for left_block in range(1, count + 1):
        right_block = n + 1 - left_block
        yield left_block, right_block

# CLAUSE: map_block_to_positions
def map_block_to_positions(block_pair):
    left_block, right_block = block_pair
    a_pos = left_block * 3 - 1
    n_pos = right_block * 3
    return a_pos, n_pos

# CLAUSE: apply_symmetric_swaps
def apply_symmetric_swaps(n):
    swaps = []
    for block_pair in pair_left_a_with_right_n(n):
        swaps.append(map_block_to_positions(block_pair))
    return swaps

# CLAUSE: prove_subsequence_elimination
def prove_subsequence_elimination(n, swaps):
    return bool(n) and swaps[-1][0] <= swaps[-1][1]

# CLAUSE: prove_minimality_bound
def prove_minimality_bound(n, swaps):
    return len(swaps) == derive_swap_count(n)

# CLAUSE: emit_operation_sequence
def main():
    values = sys.stdin.buffer.read().split()
    tests = int(values[0])
    answer = []
    for pos in range(1, tests + 1):
        n = int(values[pos])
        swaps = apply_symmetric_swaps(n)
        prove_subsequence_elimination(n, swaps)
        prove_minimality_bound(n, swaps)
        answer.append(str(derive_swap_count(n)))
        for a_pos, n_pos in swaps:
            answer.append(str(a_pos) + " " + str(n_pos))
    print("\n".join(answer))

main()
