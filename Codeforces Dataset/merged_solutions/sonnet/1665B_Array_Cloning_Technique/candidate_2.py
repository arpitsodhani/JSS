# CLAUSE: setup_environment
import sys
from collections import Counter

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(tokens[pos])
        pos += 1
        freq = Counter()
        best = 0
        for x in tokens[pos:pos + n]:
            freq[x] += 1
            if freq[x] > best:
                best = freq[x]
        pos += n
        ops = 0
        have = best
        while have < n:
            take = have if have <= n - have else n - have
            ops += take + 1
            have += take
        out.append(str(ops))
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
