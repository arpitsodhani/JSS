# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from collections import Counter

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    bars = data[1:1 + n]

    counts = Counter(bars)
    print(max(counts.values()), len(counts))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
