import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    
    used_vertical = [False] * (n + 1)
    used_horizontal = [False] * (n + 1)
    result = []
    
    idx = 1
    for day in range(1, n * n + 1):
        x = data[idx]
        y = data[idx + 1]
        idx += 2
        
        if not used_vertical[x] and not used_horizontal[y]:
            used_vertical[x] = True
            used_horizontal[y] = True
            result.append(day)
    
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
