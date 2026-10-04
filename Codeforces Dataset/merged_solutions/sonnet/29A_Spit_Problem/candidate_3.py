# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def has_pair(items):
    positions = {}
    for x, d in items:
        positions.setdefault(x, set()).add(d)
    for x, d in items:
        target = x + d
        if d != 0 and target in positions and -d in positions[target]:
            return True
    return False

def main():
    nums = [int(v) for v in sys.stdin.read().split()]
    if not nums:
        return
    pairs = [(nums[i], nums[i + 1]) for i in range(1, 1 + 2 * nums[0], 2)]
    sys.stdout.write("YES" if has_pair(pairs) else "NO")

# CLAUSE: finish_program
main()
