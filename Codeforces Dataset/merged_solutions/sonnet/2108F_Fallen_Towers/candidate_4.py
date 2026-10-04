# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def test_target(a, x):
    n = len(a)
    remove_at = [0] * (n + 1)
    cur = 0
    base = n - x
    for pos, val in enumerate(a):
        cur -= remove_at[pos]
        goal = max(0, pos - base)
        if cur < goal:
            return False
        length = val + cur - goal
        cur += 1
        cut = pos + length + 1
        if cut < n:
            remove_at[cut] += 1
    return True

def process(tokens):
    k = 1
    cases = tokens[0]
    lines = []
    for _ in range(cases):
        n = tokens[k]
        k += 1
        a = tokens[k:k + n]
        k += n
        low = 1
        high = n + 1
        while low + 1 < high:
            middle = (low + high) >> 1
            if test_target(a, middle):
                low = middle
            else:
                high = middle
        lines.append(str(low))
    return lines

def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    sys.stdout.write("\n".join(process(nums)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
