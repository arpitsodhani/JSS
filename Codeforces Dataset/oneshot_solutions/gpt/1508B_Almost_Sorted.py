import sys

def solve_case(n, k):
    if n <= 61:
        total = 1 << (n - 1)
        if k > total:
            return "-1"
    else:
        total = 1 << 60
        if k > total:
            return "-1"

    ans = []
    cur = 1
    rem = n

    while rem > 0:
        length = 1
        while length < rem:
            rest = rem - length
            cnt = 1 << min(rest - 1, 60)
            if k > cnt:
                k -= cnt
                length += 1
            else:
                break

        for x in range(cur + length - 1, cur - 1, -1):
            ans.append(str(x))

        cur += length
        rem -= length

    return " ".join(ans)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    out = []
    idx = 1

    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        out.append(solve_case(n, k))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
