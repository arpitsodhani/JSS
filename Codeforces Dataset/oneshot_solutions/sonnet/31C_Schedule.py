import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    
    intervals = []
    idx = 1
    for i in range(1, n + 1):
        l = data[idx]
        r = data[idx + 1]
        idx += 2
        intervals.append((l, r, i))
    
    intervals.sort()
    
    bad = []
    for i in range(n - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            bad.append(i)
    
    def can_remove(pos):
        if pos > 0 and pos + 1 < n:
            return intervals[pos - 1][1] <= intervals[pos + 1][0]
        return True
    
    answer = []
    
    if not bad:
        answer = list(range(1, n + 1))
    elif len(bad) == 1:
        i = bad[0]
        for pos in (i, i + 1):
            if can_remove(pos):
                answer.append(intervals[pos][2])
    elif len(bad) == 2 and bad[1] == bad[0] + 1:
        pos = bad[0] + 1
        if can_remove(pos):
            answer.append(intervals[pos][2])
    
    answer.sort()
    print(len(answer))
    if answer:
        print(' '.join(map(str, answer)))

if __name__ == "__main__":
    main()
