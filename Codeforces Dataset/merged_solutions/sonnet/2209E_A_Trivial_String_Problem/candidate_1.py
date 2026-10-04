# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def z_function(a):
    n = len(a)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and a[z[i]] == a[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        q = int(data[idx + 1])
        idx += 2
        
        s = data[idx].decode()
        idx += 1
        
        answers = [[] for _ in range(n)]
        queries = []
        for qi in range(q):
            l = int(data[idx]) - 1
            r = int(data[idx + 1]) - 1
            idx += 2
            queries.append((l, r))
            answers[l].append((r, qi))
        
        result = [0] * q
        
        for start in range(n):
            if not answers[start]:
                continue
            
            cur = s[start:]
            m = len(cur)
            z = z_function(cur)
            z[0] = m
            
            dp = [0] * (m + 1)
            pref = [0] * (m + 1)
            
            for length in range(1, m + 1):
                best = 1
                for prev in range(length):
                    part = length - prev
                    if z[prev] >= part:
                        val = dp[prev] + 1
                        if val > best:
                            best = val
                dp[length] = best
                pref[length] = pref[length - 1] + best
            
            for r, qi in answers[start]:
                result[qi] = pref[r - start + 1]
        
        out.extend(map(str, result))
    
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
