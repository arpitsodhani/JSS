import sys
from collections import defaultdict

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    weights = data[1:1 + n]
    
    count = defaultdict(int)
    for w in weights:
        count[w] += 1
    
    answer = 0
    carry = 0
    
    max_power = max(weights) if weights else 0
    limit = max_power + n.bit_length() + 2
    
    for p in range(limit + 1):
        total = count[p] + carry
        answer += total & 1
        carry = total >> 1
    
    while carry:
        answer += carry & 1
        carry >>= 1
    
    print(answer)

if __name__ == "__main__":
    main()
