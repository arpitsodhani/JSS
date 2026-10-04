# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve_group(s, start, m, queries, out):
    pi = [0] * m
    b = [0] * m

    for i in range(1, m):
        ch = s[start + i]
        j = pi[i - 1]
        while j and ch != s[start + j]:
            j = pi[j - 1]
        if ch == s[start + j]:
            j += 1
        pi[i] = j
        if j:
            if pi[j - 1] == 0:
                b[i] = j
            else:
                b[i] = b[j - 1]

    queries.sort()
    ptr = 0
    total = 0

    for i in range(m):
        bi = b[i]
        if bi == 0:
            v = 1
        else:
            v = pi[i - bi] + 1
        pi[i] = v
        total += v

        length = i + 1
        while ptr < len(queries) and queries[ptr][0] == length:
            out[queries[ptr][1]] = total
            ptr += 1

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    t = int(next(it))
    ans_all = []

    for _ in range(t):
        n = int(next(it))
        q = int(next(it))
        s = next(it)

        groups = {}
        out = [0] * q

        for idx in range(q):
            l = int(next(it)) - 1
            r = int(next(it))
            groups.setdefault(l, []).append((r - l, idx))

        for l, queries in groups.items():
            m = max(x[0] for x in queries)
            solve_group(s, l, m, queries, out)

        ans_all.extend(map(str, out))

    sys.stdout.write("\n".join(ans_all))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
