# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 1.00]
def solve_case(n, y, prices):
    m = max(prices)
    if m == 1:
        return n

    freq = [0] * (m + 1)
    for value in prices:
        freq[value] += 1

    pref = [0] * (m + 1)
    for i in range(1, m + 1):
        pref[i] = pref[i - 1] + freq[i]

    best = -10**30
    for x in range(2, m + 1):
        total = 0
        reused = 0
        new_value = 1
        left = 1
        while left <= m:
            right = left + x - 1
            if right > m:
                right = m
            count = pref[right] - pref[left - 1]
            if count:
                total += count * new_value
                if new_value <= m:
                    available = freq[new_value]
                    if available:
                        reused += available if available < count else count
            left += x
            new_value += 1
        gain = total - y * (n - reused)
        if gain > best:
            best = gain
    return best

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    out = []
    for _ in range(t):
        n = data[pos]
        y = data[pos + 1]
        pos += 2
        prices = data[pos:pos + n]
        pos += n
        out.append(str(solve_case(n, y, prices)))
    sys.stdout.write("\n".join(out))


# Clause finish_program [Confidence: 0.40]
main()


