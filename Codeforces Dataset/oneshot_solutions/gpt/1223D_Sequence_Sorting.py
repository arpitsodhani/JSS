import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    p = 1
    out = []

    for _ in range(t):
        n = data[p]
        p += 1
        a = data[p:p + n]
        p += n

        first = {}
        last = {}

        for i, x in enumerate(a):
            if x not in first:
                first[x] = i
            last[x] = i

        vals = sorted(first)
        best = cur = 1

        for i in range(1, len(vals)):
            prev = vals[i - 1]
            now = vals[i]
            if last[prev] < first[now]:
                cur += 1
            else:
                cur = 1
            if cur > best:
                best = cur

        out.append(str(len(vals) - best))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
