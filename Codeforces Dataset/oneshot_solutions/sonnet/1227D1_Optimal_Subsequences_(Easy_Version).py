import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    
    n = int(data[idx])
    idx += 1
    
    a = list(map(int, data[idx:idx + n]))
    idx += n
    
    order = sorted(range(n), key=lambda i: (-a[i], i))
    
    optimal = [[] for _ in range(n + 1)]
    chosen = []
    for k in range(1, n + 1):
        chosen.append(order[k - 1])
        optimal[k] = [a[i] for i in sorted(chosen)]
    
    m = int(data[idx])
    idx += 1
    
    ans = []
    for _ in range(m):
        k = int(data[idx])
        pos = int(data[idx + 1])
        idx += 2
        ans.append(str(optimal[k][pos - 1]))
    
    print('\n'.join(ans))

if __name__ == "__main__":
    main()
