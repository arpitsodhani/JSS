import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    groups = [[], [], [], []]

    idx = 2
    for _ in range(n):
        w = data[idx]
        c = data[idx + 1]
        idx += 2
        groups[w].append(c)

    pref = []
    for w in range(4):
        groups[w].sort(reverse=True)
        p = [0]
        s = 0
        for x in groups[w]:
            s += x
            p.append(s)
        pref.append(p)

    a = len(groups[1])
    b = len(groups[2])
    c = len(groups[3])

    limit12 = min(m, a + 2 * b)
    best12 = [0] * (limit12 + 1)

    j = 0
    for cap in range(limit12 + 1):
        if j > b:
            j = b
        if 2 * j > cap:
            j = cap // 2

        def val(x):
            return pref[2][x] + pref[1][min(a, cap - 2 * x)]

        while j < b and 2 * (j + 1) <= cap and val(j + 1) >= val(j):
            j += 1

        best12[cap] = val(j)

    ans = 0
    max3 = min(c, m // 3)
    for k in range(max3 + 1):
        rem = m - 3 * k
        if rem > limit12:
            rem = limit12
        cur = pref[3][k] + best12[rem]
        if cur > ans:
            ans = cur

    print(ans)

if __name__ == "__main__":
    main()
