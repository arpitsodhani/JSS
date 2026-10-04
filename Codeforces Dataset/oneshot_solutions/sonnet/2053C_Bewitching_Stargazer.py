import sys

def calc(length, k):
    if length < k:
        return 0, 0
    
    half = length // 2
    sub_sum, sub_count = calc(half, k)
    
    if length % 2 == 0:
        return 2 * sub_sum + sub_count * half, 2 * sub_count
    else:
        mid = half + 1
        return mid + 2 * sub_sum + sub_count * mid, 1 + 2 * sub_count

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []
    
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        
        result, _ = calc(n, k)
        ans.append(str(result))
    
    print('\n'.join(ans))

if __name__ == "__main__":
    main()
