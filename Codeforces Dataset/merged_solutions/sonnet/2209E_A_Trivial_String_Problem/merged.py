# Clause setup_environment [Confidence: 0.60]
import sys

def z_for_suffix(s, start):
    m = len(s) - start
    z = [0] * m
    left = 0
    right = -1
    for i in range(1, m):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])
        while i + z[i] < m and s[start + z[i]] == s[start + i + z[i]]:
            z[i] += 1
        new_right = i + z[i] - 1
        if new_right > right:
            left = i
            right = new_right
    if m:
        z[0] = m
    return z

def cumulative_values(z):
    n = len(z)
    dp = [0] * (n + 1)
    pref = [0] * (n + 1)
    for length in range(1, n + 1):
        candidates = 1
        split = length - 1
        while split >= 0:
            block = length - split
            if z[split] >= block:
                cur = dp[split] + 1
                if cur > candidates:
                    candidates = cur
            split -= 1
        dp[length] = candidates
        pref[length] = pref[length - 1] + candidates
    return pref


# Clause solve_logic [Confidence: 0.80]
def main():
    data = sys.stdin.buffer.read().split()
    k = 0
    tc = int(data[k])
    k += 1
    lines = []
    for _ in range(tc):
        n = int(data[k])
        q = int(data[k + 1])
        k += 2
        s = data[k]
        k += 1
        grouped = [[] for _ in range(n)]
        for index in range(q):
            l = int(data[k]) - 1
            r = int(data[k + 1]) - 1
            k += 2
            grouped[l].append((index, r))
        answers = [0] * q
        needed = [i for i, group in enumerate(grouped) if group]
        for l in needed:
            pref = cumulative_values(z_for_suffix(s, l))
            for index, r in grouped[l]:
                answers[index] = pref[r - l + 1]
        for value in answers:
            lines.append(str(value))
    sys.stdout.write("\n".join(lines))


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


