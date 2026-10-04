# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 0.60]
def mex_from_owned(seen):
    x = 0
    while x in seen:
        x += 1
    return x

def main():
    items = sys.stdin.read().split()
    t = int(items[0])
    p = 1
    ans = []
    for _ in range(t):
        n = int(items[p])
        p += 1
        first = set()
        second = set()
        for i in range(p, p + n):
            v = int(items[i])
            if v not in first:
                first.add(v)
            else:
                second.add(v)
        p += n
        ans.append(str(mex_from_owned(first) + mex_from_owned(second)))


# Clause finish_program [Confidence: 0.80]
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()


