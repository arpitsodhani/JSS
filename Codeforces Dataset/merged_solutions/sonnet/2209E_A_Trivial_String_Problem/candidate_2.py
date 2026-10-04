# CLAUSE: setup_environment
import sys

def z_values(seq):
    n = len(seq)
    z = [0] * n
    left = 0
    right = 0
    for i in range(1, n):
        if i <= right:
            v = right - i + 1
            old = z[i - left]
            z[i] = old if old < v else v
        while i + z[i] < n and seq[z[i]] == seq[i + z[i]]:
            z[i] += 1
        end = i + z[i] - 1
        if end > right:
            left = i
            right = end
    if n:
        z[0] = n
    return z

# CLAUSE: solve_logic
def solve():
    data = sys.stdin.buffer.read().split()
    at = 0
    tests = int(data[at])
    at += 1
    all_out = []
    for _ in range(tests):
        n = int(data[at])
        q = int(data[at + 1])
        at += 2
        s = data[at]
        at += 1
        by_left = [[] for _ in range(n)]
        ans = [0] * q
        for qi in range(q):
            l = int(data[at]) - 1
            r = int(data[at + 1]) - 1
            at += 2
            by_left[l].append((r, qi))
        for start, bucket in enumerate(by_left):
            if not bucket:
                continue
            tail = s[start:]
            m = n - start
            z = z_values(tail)
            dp = [0] * (m + 1)
            pref = [0] * (m + 1)
            for length in range(1, m + 1):
                best = 1
                for prev in range(length):
                    part = length - prev
                    if z[prev] >= part:
                        value = dp[prev] + 1
                        if value > best:
                            best = value
                dp[length] = best
                pref[length] = pref[length - 1] + best
            for r, qi in bucket:
                ans[qi] = pref[r - start + 1]
        all_out.extend(str(x) for x in ans)
    return "\n".join(all_out)

# CLAUSE: finish_program
if __name__ == "__main__":
    sys.stdout.write(solve())
