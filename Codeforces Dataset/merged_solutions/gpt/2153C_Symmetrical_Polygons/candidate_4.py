# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        a.sort()

        half = 0
        pairs = 0
        odd = []

        i = 0
        while i < n:
            j = i + 1
            while j < n and a[j] == a[i]:
                j += 1
            c = j - i
            pairs += c // 2
            half += a[i] * (c // 2)
            if c % 2:
                odd.append(a[i])
            i = j

        base = 2 * half
        ans = base if pairs > 1 else 0

        for x in odd:
            if base > x:
                v = base + x
                if v > ans:
                    ans = v

        for i in range(1, len(odd)):
            if base > odd[i] - odd[i - 1]:
                v = base + odd[i] + odd[i - 1]
                if v > ans:
                    ans = v

        out.append(str(ans))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
