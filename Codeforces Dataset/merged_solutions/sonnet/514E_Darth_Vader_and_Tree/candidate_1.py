# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

MOD = 10 ** 9 + 7

def multiply(a, b):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for k in range(n):
            if a[i][k]:
                value = a[i][k]
                bk = b[k]
                row = result[i]
                for j in range(n):
                    row[j] = (row[j] + value * bk[j]) % MOD
    
    return result

def apply_matrix(mat, vec):
    n = len(vec)
    result = [0] * n
    
    for i in range(n):
        total = 0
        row = mat[i]
        for j in range(n):
            total += row[j] * vec[j]
        result[i] = total % MOD
    
    return result

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    
    n = data[0]
    x = data[1]
    distances = data[2:2 + n]
    
    max_d = max(distances)
    count = [0] * (max_d + 1)
    for d in distances:
        count[d] += 1
    
    size = max_d + 1
    trans = [[0] * size for _ in range(size)]
    
    for d in range(1, max_d + 1):
        trans[0][d - 1] = count[d] % MOD
    
    for i in range(1, max_d):
        trans[i][i - 1] = 1
    
    for j in range(max_d):
        trans[max_d][j] = trans[0][j]
    trans[max_d][max_d] = 1
    
    state = [0] * size
    state[0] = 1
    state[max_d] = 1
    
    while x > 0:
        if x & 1:
            state = apply_matrix(trans, state)
        trans = multiply(trans, trans)
        x >>= 1
    
    print(state[max_d] % MOD)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
