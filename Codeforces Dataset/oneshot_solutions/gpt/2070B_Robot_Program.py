import sys

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        x = int(data[idx + 1])
        k = int(data[idx + 2])
        s = data[idx + 3]
        idx += 4

        pos = 0
        first_hit = -1
        first_zero_from_zero = -1

        for i, c in enumerate(s, 1):
            pos += 1 if c == 'R' else -1

            if first_hit == -1 and x + pos == 0:
                first_hit = i

            if first_zero_from_zero == -1 and pos == 0:
                first_zero_from_zero = i

        if first_hit == -1 or first_hit > k:
            out.append("0")
            continue

        ans = 1
        remaining = k - first_hit

        if first_zero_from_zero != -1:
            ans += remaining // first_zero_from_zero

        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
