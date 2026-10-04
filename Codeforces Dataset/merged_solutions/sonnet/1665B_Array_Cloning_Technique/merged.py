# Clause setup_environment [Confidence: 0.60]
import sys


# Clause solve_logic [Confidence: 0.80]
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


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


