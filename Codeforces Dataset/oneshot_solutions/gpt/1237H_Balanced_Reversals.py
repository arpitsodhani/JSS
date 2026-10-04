import sys

def kind(x, y):
    if x == y:
        return x
    return '2'

def orient(x, y):
    return 0 if x == '0' and y == '1' else 1

def apply(arr, k):
    arr[:k] = arr[:k][::-1]
    for i in range(k):
        if arr[i][0] == '2':
            arr[i] = ('2', arr[i][1] ^ 1)

def solve(a, b):
    n = len(a)
    m = n // 2
    cur = []
    target = []
    ca = {'0': 0, '1': 0, '2': 0}
    cb = {'0': 0, '1': 0, '2': 0}

    for i in range(0, n, 2):
        t = kind(a[i], a[i + 1])
        ca[t] += 1
        cur.append((t, orient(a[i], a[i + 1]) if t == '2' else 0))

        t = kind(b[i], b[i + 1])
        cb[t] += 1
        target.append((t, orient(b[i], b[i + 1]) if t == '2' else 0))

    if ca != cb:
        return None

    ans = []
    for pos in range(m - 1, -1, -1):
        need = target[pos]

        if cur[pos] == need:
            continue

        idx = -1
        for i in range(pos + 1):
            if cur[i] == need:
                idx = i
                break

        if idx == -1 and need[0] == '2':
            for i in range(pos + 1):
                if cur[i][0] == '2' and cur[i][1] != need[1]:
                    idx = i
                    break

            if idx > 0:
                ans.append(idx * 2)
                apply(cur, idx)
            ans.append(2)
            apply(cur, 1)
            idx = 0

        if idx == -1:
            for i in range(pos + 1):
                if cur[i][0] == need[0]:
                    idx = i
                    break

        if idx > 0:
            ans.append((idx + 1) * 2)
            apply(cur, idx + 1)

        if pos > 0:
            ans.append((pos + 1) * 2)
            apply(cur, pos + 1)

    if cur != target or len(ans) > n + 1:
        return None
    return ans

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    t = int(data[0])
    out = []
    p = 1
    for _ in range(t):
        a = data[p]
        b = data[p + 1]
        p += 2

        ans = solve(a, b)
        if ans is None:
            out.append("-1")
        else:
            out.append(str(len(ans)))
            if ans:
                out.append(" ".join(map(str, ans)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
