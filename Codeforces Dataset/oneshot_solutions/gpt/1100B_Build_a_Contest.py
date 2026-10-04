import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    a = data[2:2 + m]

    cnt = [0] * (n + 1)
    freq = [0] * (m + 2)
    freq[0] = n

    used = 0
    active = 0
    ans = []

    for x in a:
        old = cnt[x]
        if old == used:
            active += 1

        freq[old] -= 1
        cnt[x] = old + 1
        freq[old + 1] += 1

        if active == n:
            ans.append('1')
            used += 1
            active -= freq[used]
        else:
            ans.append('0')

    sys.stdout.write(''.join(ans))

if __name__ == "__main__":
    main()
