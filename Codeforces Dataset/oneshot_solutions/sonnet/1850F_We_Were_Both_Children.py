import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        freq = [0] * (n + 1)
        for _ in range(n):
            a = data[idx]
            idx += 1
            if a <= n:
                freq[a] += 1
        
        caught = [0] * (n + 1)
        for hop in range(1, n + 1):
            if freq[hop]:
                for pos in range(hop, n + 1, hop):
                    caught[pos] += freq[hop]
        
        results.append(str(max(caught)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
