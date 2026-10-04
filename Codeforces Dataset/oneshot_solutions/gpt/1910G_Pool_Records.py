import sys

def valid(t):
    n = len(t)
    if n == 0:
        return False
    if t[0] <= 0:
        return False
    for i in range(1, n):
        if t[i] <= t[i - 1]:
            return False

    q = t[0]
    p = None
    for x in t:
        if x % q != 0:
            p = x
            break

    if p is None:
        for i, x in enumerate(t, 1):
            if x != q * i:
                return False
        return True

    i = j = 1
    res = []
    while len(res) < n:
        a = q * i
        b = p * j
        if a < b:
            res.append(a)
            i += 1
        elif b < a:
            res.append(b)
            j += 1
        else:
            res.append(a)
            i += 1
            j += 1

    return res == t

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    tc = data[0]
    pos = 1
    ans = []

    for _ in range(tc):
        n = data[pos]
        pos += 1
        t = data[pos:pos + n]
        pos += n
        ans.append("VALID" if valid(t) else "INVALID")

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
