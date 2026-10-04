import sys

MOD = 10 ** 9 + 7

def multiply(a, b, m):
    result = [[0] * m for _ in range(m)]
    for i in range(m):
        row = a[i]
        for k in range(m):
            if row[k]:
                value = row[k]
                brow = b[k]
                for j in range(m):
                    result[i][j] = (result[i][j] + value * brow[j]) % MOD
    return result

def power(matrix, exp, m):
    result = [[0] * m for _ in range(m)]
    for i in range(m):
        result[i][i] = 1
    
    while exp:
        if exp & 1:
            result = multiply(result, matrix, m)
        matrix = multiply(matrix, matrix, m)
        exp >>= 1
    
    return result

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, l, m = data[0], data[1], data[2]
    
    a = data[3:3 + n]
    b = data[3 + n:3 + 2 * n]
    c = data[3 + 2 * n:3 + 3 * n]
    
    start = [0] * m
    for x in a:
        start[x % m] += 1
    
    trans = [[0] * m for _ in range(m)]
    for x in b:
        shift = x % m
        for r in range(m):
            trans[r][(r + shift) % m] += 1
    
    mat = power(trans, l - 2, m)
    
    middle = [0] * m
    for i in range(m):
        if start[i]:
            for j in range(m):
                middle[j] = (middle[j] + start[i] * mat[i][j]) % MOD
    
    answer = 0
    for x in c:
        answer = (answer + middle[(-x) % m]) % MOD
    
    print(answer)

if __name__ == "__main__":
    main()
