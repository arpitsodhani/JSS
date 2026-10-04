# Clause setup_environment [Confidence: 0.60]
import sys

MOD = 998244353


# Clause solve_logic [Confidence: 0.40]
def number_of_subsequences(arr):
    totals = [0]
    ways = [1]
    where = {0: 0}

    for x in arr:
        old_len = len(totals)
        additions = []

        for i in range(old_len):
            s = totals[i]
            w = ways[i]
            if x == 0:
                additions.append((s, w))
            elif s == x:
                additions.append((s + x, w))
            elif s == 3 * x:
                additions.append((s, w))

        for s, w in additions:
            j = where.get(s)
            if j is None:
                where[s] = len(totals)
                totals.append(s)
                ways.append(w % MOD)
            else:
                ways[j] = (ways[j] + w) % MOD

    return sum(ways) % MOD


# Clause finish_program [Confidence: 0.80]
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    t = int(raw[0])
    p = 1
    answers = []

    for _ in range(t):
        n = int(raw[p])
        p += 1
        arr = tuple(map(int, raw[p:p + n]))
        p += n
        answers.append(str(number_of_subsequences(arr)))

    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    main()


