import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    idx = 1
    
    if n == 1:
        print(1)
        return
    
    ans = []
    for i in range(n):
        row_max = 0
        for j in range(n):
            row_max = max(row_max, data[idx])
            idx += 1
        ans.append(row_max)
    
    count = [0] * (n + 1)
    for x in ans:
        count[x] += 1
    
    missing = 1
    while count[missing] > 0:
        missing += 1
    
    for i in range(n):
        if count[ans[i]] > 1:
            count[ans[i]] -= 1
            ans[i] = missing
            break
    
    print(' '.join(map(str, ans)))

main()
