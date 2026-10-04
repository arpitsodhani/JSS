import sys

def build_prime(limit):
    is_prime = [True] * (limit + 1)
    if limit >= 0:
        is_prime[0] = False
    if limit >= 1:
        is_prime[1] = False
    
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for x in range(p * p, limit + 1, p):
                is_prime[x] = False
        p += 1
    
    return is_prime

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    tests = []
    max_a = 0
    
    for _ in range(t):
        n = data[idx]
        e = data[idx + 1]
        idx += 2
        
        a = data[idx:idx + n]
        idx += n
        
        tests.append((n, e, a))
        max_a = max(max_a, max(a))
    
    is_prime = build_prime(max_a)
    answers = []
    
    for n, e, a in tests:
        result = 0
        
        for start in range(e):
            chain = []
            pos = start
            while pos < n:
                chain.append(a[pos])
                pos += e
            
            m = len(chain)
            left_ones = [0] * m
            count = 0
            
            for i in range(m):
                if chain[i] == 1:
                    count += 1
                else:
                    count = 0
                left_ones[i] = count
            
            right_ones = [0] * m
            count = 0
            
            for i in range(m - 1, -1, -1):
                if chain[i] == 1:
                    count += 1
                else:
                    count = 0
                right_ones[i] = count
            
            for i in range(m):
                if is_prime[chain[i]]:
                    left = left_ones[i - 1] if i > 0 else 0
                    right = right_ones[i + 1] if i + 1 < m else 0
                    result += (left + 1) * (right + 1) - 1
        
        answers.append(str(result))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
