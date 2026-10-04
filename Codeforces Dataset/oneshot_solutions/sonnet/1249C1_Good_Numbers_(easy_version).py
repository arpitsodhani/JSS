import sys

def next_good(n):
    digits = []
    x = n
    
    while x > 0:
        digits.append(x % 3)
        x //= 3
    
    digits.append(0)
    
    pos = -1
    for i, d in enumerate(digits):
        if d == 2:
            pos = i
    
    if pos == -1:
        return n
    
    carry_pos = pos + 1
    while digits[carry_pos] == 1:
        digits[carry_pos] = 0
        carry_pos += 1
    
    digits[carry_pos] = 1
    
    for i in range(carry_pos):
        digits[i] = 0
    
    result = 0
    power = 1
    for d in digits:
        result += d * power
        power *= 3
    
    return result

def main():
    data = sys.stdin.read().split()
    q = int(data[0])
    
    ans = []
    for i in range(1, q + 1):
        n = int(data[i])
        ans.append(str(next_good(n)))
    
    print('\n'.join(ans))

if __name__ == "__main__":
    main()
