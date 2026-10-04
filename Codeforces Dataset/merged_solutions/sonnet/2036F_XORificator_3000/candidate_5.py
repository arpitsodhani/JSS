# CLAUSE: setup_environment
import sys

def xor_to(n):
    if n < 0:
        return 0
    r = n % 4
    if r < 2:
        return n if r == 0 else 1
    return n + 1 if r == 2 else 0

def removed_to(n, i, k):
    if n < k:
        return 0
    period = 1 << i
    count = (n - k) // period + 1
    compressed_last = count - 1
    high_part = xor_to(compressed_last) << i
    low_part = k if count & 1 else 0
    return high_part ^ low_part

# CLAUSE: solve_logic
def run():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    result = [""] * n
    p = 1
    for case_index in range(n):
        l = int(data[p])
        r = int(data[p + 1])
        i = int(data[p + 2])
        k = int(data[p + 3])
        p += 4
        left_total = xor_to(l - 1)
        right_total = xor_to(r)
        left_removed = removed_to(l - 1, i, k)
        right_removed = removed_to(r, i, k)
        result[case_index] = str(right_total ^ left_total ^ right_removed ^ left_removed)
    print("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    run()
