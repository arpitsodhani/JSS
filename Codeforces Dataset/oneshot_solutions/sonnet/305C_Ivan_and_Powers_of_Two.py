import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    powers = data[1:1 + n]
    
    ones = 0
    carry = 0
    prev = powers[0]
    i = 0
    
    while i < n:
        e = powers[i]
        
        if carry:
            gap = e - prev
            if gap > 0:
                shift = min(gap, carry.bit_length() + 1)
                for _ in range(shift):
                    ones += carry & 1
                    carry >>= 1
                if gap > shift:
                    carry = 0
        
        cnt = 0
        while i < n and powers[i] == e:
            cnt += 1
            i += 1
        
        carry += cnt
        prev = e
    
    highest = prev
    while carry:
        ones += carry & 1
        carry >>= 1
        highest += 1
    
    bit_length = highest
    print(bit_length - ones)

if __name__ == "__main__":
    main()
