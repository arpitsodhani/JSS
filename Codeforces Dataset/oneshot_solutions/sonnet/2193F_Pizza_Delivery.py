import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    answers = []
    
    for _ in range(t):
        n = data[idx]
        ax = data[idx + 1]
        ay = data[idx + 2]
        bx = data[idx + 3]
        by = data[idx + 4]
        idx += 5
        
        xs = data[idx:idx + n]
        idx += n
        ys = data[idx:idx + n]
        idx += n
        
        groups = {}
        for x, y in zip(xs, ys):
            if x not in groups:
                groups[x] = [y, y]
            else:
                groups[x][0] = min(groups[x][0], y)
                groups[x][1] = max(groups[x][1], y)
        
        low_prev = high_prev = ay
        dp_low = dp_high = 0
        
        for x in sorted(groups):
            low, high = groups[x]
            width = high - low
            
            new_low = min(dp_low + abs(low_prev - high),
                          dp_high + abs(high_prev - high)) + width
            new_high = min(dp_low + abs(low_prev - low),
                           dp_high + abs(high_prev - low)) + width
            
            low_prev, high_prev = low, high
            dp_low, dp_high = new_low, new_high
        
        vertical = min(dp_low + abs(low_prev - by),
                       dp_high + abs(high_prev - by))
        answers.append(str((bx - ax) + vertical))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    solve()
