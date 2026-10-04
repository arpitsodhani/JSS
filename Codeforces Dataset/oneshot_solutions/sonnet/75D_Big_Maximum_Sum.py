import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    m = data[idx + 1]
    idx += 2
    
    total = [0] * (n + 1)
    pref = [0] * (n + 1)
    suff = [0] * (n + 1)
    best = [0] * (n + 1)
    
    for i in range(1, n + 1):
        length = data[idx]
        idx += 1
        arr = data[idx:idx + length]
        idx += length
        
        s = sum(arr)
        total[i] = s
        
        cur = 0
        max_pref = -10**30
        for x in arr:
            cur += x
            max_pref = max(max_pref, cur)
        pref[i] = max_pref
        
        cur = 0
        max_suff = -10**30
        for x in reversed(arr):
            cur += x
            max_suff = max(max_suff, cur)
        suff[i] = max_suff
        
        cur_best = arr[0]
        cur_end = arr[0]
        for x in arr[1:]:
            cur_end = max(x, cur_end + x)
            cur_best = max(cur_best, cur_end)
        best[i] = cur_best
    
    order = data[idx:idx + m]
    
    first = order[0]
    answer = best[first]
    ending = suff[first]
    
    for block in order[1:]:
        answer = max(answer, best[block], ending + pref[block])
        ending = max(suff[block], ending + total[block])
    
    print(answer)

if __name__ == "__main__":
    main()
