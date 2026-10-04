import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[0], data[1]
    a = data[2:2 + n]

    mn = min(a)
    mx = max(a)

    if k >= mn - 1:
        print(mn)
        return

    pref = [0] * (mx + 1)
    for x in a:
        pref[x] += 1

    s = 0
    for i in range(mx + 1):
        s += pref[i]
        pref[i] = s

    for d in range(mn, 0, -1):
        if k >= d - 1:
            print(d)
            return

        ok = True
        l = d + k + 1
        bad_len = d - k - 1

        while l <= mx:
            r = l + bad_len - 1
            if r > mx:
                r = mx
            if pref[r] - pref[l - 1]:
                ok = False
                break
            l += d

        if ok:
            print(d)
            return

if __name__ == "__main__":
    main()
