import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    a = data[1:1 + n]
    
    segments = []
    seen = set()
    start = 1
    
    for i, x in enumerate(a, 1):
        if x in seen:
            segments.append([start, i])
            start = i + 1
            seen.clear()
        else:
            seen.add(x)
    
    if not segments:
        print(-1)
        return
    
    segments[-1][1] = n
    
    print(len(segments))
    for l, r in segments:
        print(l, r)

if __name__ == "__main__":
    main()
