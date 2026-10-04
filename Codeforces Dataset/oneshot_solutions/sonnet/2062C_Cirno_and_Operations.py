import sys

def solve(a):
    memo = {}
    
    def rec(arr):
        t = tuple(arr)
        if t in memo:
            return memo[t]
        
        n = len(arr)
        if n == 1:
            return arr[0]
        
        # Option: stop here
        result = sum(arr)
        
        # Option: apply difference
        diff = [arr[i+1] - arr[i] for i in range(n-1)]
        result = max(result, rec(diff))
        
        # Option: apply difference to reversed array
        rev = arr[::-1]
        diff_rev = [rev[i+1] - rev[i] for i in range(n-1)]
        result = max(result, rec(diff_rev))
        
        memo[t] = result
        return result
    
    return rec(a)

def main():
    input_data = sys.stdin.buffer.read().decode().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        a = list(map(int, input_data[idx:idx+n]))
        idx += n
        print(solve(a))

if __name__ == "__main__":
    main()
