import sys

def main():
    n = int(sys.stdin.readline())
    
    result = list(range(n + 1))
    used = [False] * (n + 1)
    
    primes = []
    is_composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not is_composite[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_composite[j] = True
    
    for p in reversed(primes):
        nums = []
        for x in range(p, n + 1, p):
            if not used[x]:
                nums.append(x)
        
        if len(nums) > 1:
            for i in range(len(nums)):
                result[nums[i]] = nums[(i + 1) % len(nums)]
                used[nums[i]] = True
    
    print(' '.join(map(str, result[1:])))

if __name__ == "__main__":
    main()
