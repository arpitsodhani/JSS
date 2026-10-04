# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

MOD = 998244353

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    tests = []
    max_n = 0
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        tests.append((n, a))
        max_n = max(max_n, n)
    
    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = fact[i - 1] * i % MOD
    
    out = []
    for n, a in tests:
        a.sort()
        
        if a[-1] == a[-2]:
            out.append(str(fact[n]))
            continue
        
        if a[-1] - a[-2] > 1:
            out.append("0")
            continue
        
        cnt = 0
        target = a[-1] - 1
        for x in a:
            if x == target:
                cnt += 1
        
        bad = fact[n] * pow(cnt + 1, MOD - 2, MOD) % MOD
        ans = (fact[n] - bad) % MOD
        out.append(str(ans))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
