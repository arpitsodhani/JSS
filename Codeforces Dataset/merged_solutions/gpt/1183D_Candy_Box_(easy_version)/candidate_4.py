# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from collections import Counter

    data = list(map(int, sys.stdin.buffer.read().split()))
    q = data[0]
    idx = 1
    ans = []

    for _ in range(q):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n

        freqs = sorted(Counter(a).values(), reverse=True)
        limit = 10**18
        total = 0

        for f in freqs:
            take = min(f, limit - 1)
            if take <= 0:
                break
            total += take
            limit = take

        ans.append(str(total))

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
