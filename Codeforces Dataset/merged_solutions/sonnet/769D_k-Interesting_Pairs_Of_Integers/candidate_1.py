# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    nums = data[2:2 + n]
    
    bits = 14
    size = 1 << bits
    
    if k > bits:
        print(0)
        return
    
    freq = [0] * size
    for x in nums:
        freq[x] += 1
    
    if k == 0:
        ans = 0
        for c in freq:
            ans += c * (c - 1) // 2
        print(ans)
        return
    
    masks = []
    for mask in range(size):
        if mask.bit_count() == k:
            masks.append(mask)
    
    ans = 0
    for mask in masks:
        total = 0
        for x in range(size):
            total += freq[x] * freq[x ^ mask]
        ans += total
    
    print(ans // 2)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
