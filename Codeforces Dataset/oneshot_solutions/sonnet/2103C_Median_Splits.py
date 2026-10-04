import sys

def possible(n, k, a):
    pref_sum = [0] * (n + 1)
    for i, x in enumerate(a, 1):
        val = 1 if x <= k else -1
        pref_sum[i] = pref_sum[i - 1] + val
    
    good_prefix = [False] * (n + 1)
    any_good_prefix = [False] * (n + 1)
    for i in range(1, n + 1):
        good_prefix[i] = pref_sum[i] >= (i % 2)
        any_good_prefix[i] = any_good_prefix[i - 1] or good_prefix[i]
    
    good_suffix = [False] * (n + 2)
    for i in range(1, n + 1):
        length = n - i + 1
        total = pref_sum[n] - pref_sum[i - 1]
        good_suffix[i] = total >= (length % 2)
    
    for start in range(3, n + 1):
        if good_suffix[start] and any_good_prefix[start - 2]:
            return True
    
    inf = 10 ** 18
    best = [inf, inf]
    for r in range(2, n):
        l = r - 1
        if good_prefix[l]:
            best[l % 2] = min(best[l % 2], pref_sum[l])
        
        if best[r % 2] <= pref_sum[r]:
            return True
        if best[1 - (r % 2)] <= pref_sum[r] - 1:
            return True
    
    best = [inf, inf]
    for r in range(2, n):
        l = r - 1
        best[l % 2] = min(best[l % 2], pref_sum[l])
        
        if not good_suffix[r + 1]:
            continue
        
        if best[r % 2] <= pref_sum[r]:
            return True
        if best[1 - (r % 2)] <= pref_sum[r] - 1:
            return True
    
    return False

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    ans = []
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        
        a = data[idx:idx + n]
        idx += n
        
        ans.append("YES" if possible(n, k, a) else "NO")
    
    print('\n'.join(ans))

if __name__ == "__main__":
    main()
