import sys

MOD = 1_000_000_007

def solve_case(x, s):
    # CLAUSE: track_virtual_length
    stored = [ch for ch in s]
    total = len(stored)

    for idx in range(x):
        # CLAUSE: materialize_needed_prefix
        ch = stored[idx]

        # CLAUSE: extract_repeat_factor
        repeats = int(ch) - 1

        # CLAUSE: append_suffix_copies
        left_cut = idx + 1
        base_tail_len = len(stored) - left_cut

        # CLAUSE: apply_modular_growth
        total = (total + (total - left_cut) * repeats) % MOD

        # CLAUSE: limit_buffer_expansion
        add = 0
        while add < repeats and len(stored) < x:
            p = 0
            while p < base_tail_len and len(stored) < x:
                stored.append(stored[left_cut + p])
                p += 1
            add += 1

    # CLAUSE: emit_final_length
    return total % MOD

def main():
    values = sys.stdin.read().strip().split()
    t = int(values[0])
    p = 1
    res = []
    for _ in range(t):
        x = int(values[p])
        s = values[p + 1]
        p += 2
        res.append(str(solve_case(x, s)))
    sys.stdout.write("\n".join(res))

main()
