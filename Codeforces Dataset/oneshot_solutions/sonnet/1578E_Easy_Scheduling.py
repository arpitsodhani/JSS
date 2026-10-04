import sys

def solve(h, p):
    time = 0
    ready = [0] * h
    ready[0] = 1
    done = [0] * h
    total = [2**i for i in range(h)]
    
    while done != total:
        time += 1
        can_perform = p
        new_ready = [0] * h
        
        for level in range(h):
            if ready[level] > 0 and can_perform > 0:
                perform = min(ready[level], can_perform)
                done[level] += perform
                ready[level] -= perform
                can_perform -= perform
                
                if level < h - 1:
                    new_ready[level + 1] += 2 * perform
        
        for level in range(h):
            ready[level] += new_ready[level]
    
    return time

def main():
    data = sys.stdin.read().strip().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        h = int(data[idx])
        p = int(data[idx + 1])
        idx += 2
        print(solve(h, p))

if __name__ == "__main__":
    main()
