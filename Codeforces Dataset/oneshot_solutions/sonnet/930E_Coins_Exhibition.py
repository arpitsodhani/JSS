import sys

MOD = 10 ** 9 + 7
INV2 = (MOD + 1) // 2

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    idx = 0
    k = data[idx]
    n = data[idx + 1]
    m = data[idx + 2]
    idx += 3
    
    obverse_events = {}
    reverse_events = {}
    points = {0, k, k - 1}
    
    for _ in range(n):
        l = data[idx]
        r = data[idx + 1]
        idx += 2
        obverse_events.setdefault(r, []).append(l)
        points.add(r)
        points.add(l - 1)
    
    for _ in range(m):
        l = data[idx]
        r = data[idx + 1]
        idx += 2
        reverse_events.setdefault(r, []).append(l)
        points.add(r)
        points.add(l - 1)
    
    points = sorted(x for x in points if 0 < x <= k)
    
    pref_zero = {0: 1}
    pref_one = {0: 1}
    
    p_zero = 1
    p_one = 1
    pos = 0
    
    zero_limit = 0
    one_limit = 0
    
    def advance(length):
        nonlocal p_zero, p_one
        
        if length <= 0:
            return
        
        cut_zero = 0 if zero_limit == 0 else pref_one[zero_limit - 1]
        cut_one = 0 if one_limit == 0 else pref_zero[one_limit - 1]
        
        power = pow(2, length, MOD)
        total = (power * (p_zero + p_one) - (power - 1) * (cut_zero + cut_one)) % MOD
        
        next_zero = (total + cut_one - cut_zero) * INV2 % MOD
        next_one = (total - cut_one + cut_zero) * INV2 % MOD
        
        p_zero = next_zero
        p_one = next_one
    
    for x in points:
        has_event = x in obverse_events or x in reverse_events
        
        if has_event:
            advance(x - 1 - pos)
            pos = x - 1
            
            if x in obverse_events:
                zero_limit = max(zero_limit, max(obverse_events[x]))
            if x in reverse_events:
                one_limit = max(one_limit, max(reverse_events[x]))
            
            advance(1)
            pos = x
        else:
            advance(x - pos)
            pos = x
        
        pref_zero[x] = p_zero
        pref_one[x] = p_one
    
    answer = (p_zero + p_one - pref_zero[k - 1] - pref_one[k - 1]) % MOD
    print(answer)

if __name__ == "__main__":
    main()
