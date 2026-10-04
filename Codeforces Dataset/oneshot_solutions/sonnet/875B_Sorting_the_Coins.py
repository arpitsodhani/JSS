import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    order = data[1:]
    
    active = [False] * (n + 2)
    segments = 0
    result = [1]
    
    for pos in order:
        active[pos] = True
        segments += 1
        
        if active[pos - 1]:
            segments -= 1
        if active[pos + 1]:
            segments -= 1
        
        result.append(segments + 1)
    
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
