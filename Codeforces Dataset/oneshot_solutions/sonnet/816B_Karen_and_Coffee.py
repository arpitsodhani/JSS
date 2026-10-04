import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    k = data[idx + 1]
    q = data[idx + 2]
    idx += 3
    
    max_temp = 200000
    diff = [0] * (max_temp + 2)
    
    for _ in range(n):
        l = data[idx]
        r = data[idx + 1]
        idx += 2
        diff[l] += 1
        diff[r + 1] -= 1
    
    good = [0] * (max_temp + 1)
    current = 0
    for temp in range(1, max_temp + 1):
        current += diff[temp]
        good[temp] = good[temp - 1] + (1 if current >= k else 0)
    
    ans = []
    for _ in range(q):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        ans.append(str(good[b] - good[a - 1]))
    
    print('\n'.join(ans))

if __name__ == "__main__":
    main()
