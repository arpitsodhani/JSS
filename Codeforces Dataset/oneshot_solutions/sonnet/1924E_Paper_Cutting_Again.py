import sys

MOD = 10**9 + 7

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    max_need = 1
    
    idx = 1
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        k = data[idx + 2]
        idx += 3
        cases.append((n, m, k))
        max_need = max(max_need, n + m)
    
    inv = [0] * (max_need + 1)
    inv[1] = 1
    for i in range(2, max_need + 1):
        inv[i] = (MOD - MOD // i) * inv[MOD % i] % MOD
    
    answers = []
    for n, m, k in cases:
        limit = k - 1
        
        if n * m <= limit:
            answers.append("0")
            continue
        
        result = 1
        
        first_width = limit // n + 1
        if first_width < 1:
            first_width = 1
        for width in range(first_width, m):
            result += inv[width + limit // width]
            if result >= MOD:
                result -= MOD
        
        first_height = limit // m + 1
        if first_height < 1:
            first_height = 1
        for height in range(first_height, n):
            result += inv[height + limit // height]
            if result >= MOD:
                result -= MOD
        
        answers.append(str(result % MOD))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
