# CLAUSE: setup_environment
import sys

def pref(x):
    if x < 0:
        return 0
    r = x & 3
    return x if r == 0 else 1 if r == 1 else x + 1 if r == 2 else 0

def pref_bad(limit, shift, keep):
    if limit < keep:
        return 0
    m = 1 << shift
    top = (limit - keep) // m
    res = pref(top) << shift
    if top % 2 == 0:
        res ^= keep
    return res

def pref_good(limit, shift, keep):
    return pref(limit) ^ pref_bad(limit, shift, keep)

# CLAUSE: solve_logic
def solve_case(parts):
    l, r, i, k = parts
    return pref_good(r, i, k) ^ pref_good(l - 1, i, k)

def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    total = nums[0]
    chunks = (nums[p:p + 4] for p in range(1, 1 + 4 * total, 4))
    sys.stdout.write("\n".join(str(solve_case(chunk)) for chunk in chunks))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
