import sys

def main():
    MOD = 998244353
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    nums = list(map(int, input_data[1:t+1]))
    
    max_n = max(nums) if nums else 0
    
    a = [0] * (max_n + 1)
    if max_n >= 0:
        a[0] = 1
    if max_n >= 1:
        a[1] = 1
    if max_n >= 2:
        a[2] = 2
    
    for i in range(3, max_n + 1):
        a[i] = (2 * a[i - 1] + 4 * a[i - 2] - 4 * a[i - 3]) % MOD
    
    for n in nums:
        print(a[n])

if __name__ == "__main__":
    main()
