import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    
    n = data[0]
    k = data[1]
    x = data[2:2 + n]
    
    rides = 0
    pos = 0
    
    while pos < n - 1:
        next_pos = pos
        
        while next_pos + 1 < n and x[next_pos + 1] - x[pos] <= k:
            next_pos += 1
        
        if next_pos == pos:
            print(-1)
            return
        
        rides += 1
        pos = next_pos
    
    print(rides)

if __name__ == "__main__":
    main()
