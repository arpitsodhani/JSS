# CLAUSE: setup_environment
import sys

def solve_case(n, colors):
    limited = []
    for v in colors:
        limited.append(n - 1 if v >= n else v)
    limited.sort()
    m = len(limited)
    suffix_sum = [0] * (m + 1)
    for i in range(m - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + limited[i]
    ans = 0

# CLAUSE: solve_logic
    j = m
    for x in limited:
        need = n - x
        while j > 0 and limited[j - 1] >= need:
            j -= 1
        cnt = m - j
        ans += suffix_sum[j] + cnt * (x - n + 1)
        if x >= need:
            ans -= x + x - n + 1
    return ans

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    output = []
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        output.append(str(solve_case(n, data[idx:idx + m])))
        idx += m

# CLAUSE: finish_program
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
