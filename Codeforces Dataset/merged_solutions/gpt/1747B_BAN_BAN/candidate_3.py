import sys

# CLAUSE: derive_swap_count
def derive_swap_count(n):
    return n // 2 + n % 2

# CLAUSE: pair_left_a_with_right_n
def pair_left_a_with_right_n(n, count):
    left_blocks = range(count)
    return ((left_zero, n - 1 - left_zero) for left_zero in left_blocks)

# CLAUSE: map_block_to_positions
def map_block_to_positions(left_zero, right_zero):
    a_index = 3 * left_zero + 2
    n_index = 3 * right_zero + 3
    return a_index, n_index

# CLAUSE: apply_symmetric_swaps
def apply_symmetric_swaps(n):
    count = derive_swap_count(n)
    for left_zero, right_zero in pair_left_a_with_right_n(n, count):
        yield map_block_to_positions(left_zero, right_zero)

# CLAUSE: prove_subsequence_elimination
def prove_subsequence_elimination(n, count):
    return count * 2 >= n

# CLAUSE: prove_minimality_bound
def prove_minimality_bound(n, count):
    return count - 1 < (n + 1) // 2

# CLAUSE: emit_operation_sequence
def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    out_lines = []
    for n in nums[1:]:
        count = derive_swap_count(n)
        prove_subsequence_elimination(n, count)
        prove_minimality_bound(n, count)
        out_lines.append(str(count))
        out_lines += ["{} {}".format(a, b) for a, b in apply_symmetric_swaps(n)]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
