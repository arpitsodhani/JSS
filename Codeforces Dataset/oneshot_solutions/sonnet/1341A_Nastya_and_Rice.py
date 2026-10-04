import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    ans = []
    for _ in range(t):
        n = int(data[idx])
        a = int(data[idx + 1])
        b = int(data[idx + 2])
        c = int(data[idx + 3])
        d = int(data[idx + 4])
        idx += 5
        
        min_grains = n * (a - b)
        max_grains = n * (a + b)
        min_package = c - d
        max_package = c + d
        
        if max_grains < min_package or max_package < min_grains:
            ans.append("No")
        else:
            ans.append("Yes")
    
    print('\n'.join(ans))

if __name__ == "__main__":
    main()
