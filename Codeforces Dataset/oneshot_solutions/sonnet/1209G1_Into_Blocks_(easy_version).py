import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    n = int(data[0])
    q = int(data[1])
    a = list(map(int, data[2:2 + n]))
    
    first = {}
    last = {}
    freq = {}
    
    for i, x in enumerate(a):
        if x not in first:
            first[x] = i
            freq[x] = 0
        last[x] = i
        freq[x] += 1
    
    intervals = []
    for x in first:
        intervals.append((first[x], last[x], freq[x]))
    
    intervals.sort()
    
    answer = 0
    cur_r = -1
    total = 0
    best = 0
    
    for l, r, cnt in intervals:
        if l > cur_r:
            if total:
                answer += total - best
            cur_r = r
            total = cnt
            best = cnt
        else:
            cur_r = max(cur_r, r)
            total += cnt
            best = max(best, cnt)
    
    if total:
        answer += total - best
    
    print(answer)

if __name__ == "__main__":
    main()
