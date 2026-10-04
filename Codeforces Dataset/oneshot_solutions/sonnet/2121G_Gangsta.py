import sys

def solve(n, s):
    total = 0
    for l in range(n):
        count_0 = 0
        for r in range(l, n):
            if s[r] == '0':
                count_0 += 1
            length = r - l + 1
            total += max(count_0, length - count_0)
    return total

def main():
    data = sys.stdin.read().strip().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        s = data[idx]
        idx += 1
        
        result = solve(n, s)
        print(result)

if __name__ == "__main__":
    main()
