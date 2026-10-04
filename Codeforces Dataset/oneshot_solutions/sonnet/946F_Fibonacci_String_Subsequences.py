def solve():
    x = int(input())
    s = input().strip()
    m = len(s)
    MOD = 10**9 + 7
    
    # Build KMP failure function
    fail = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and s[i] != s[j]:
            j = fail[j-1]
        if s[i] == s[j]:
            j += 1
        fail[i] = j
    
    def mat_mult(A, B):
        T_A, C_A = A
        T_B, C_B = B
        T_res = [[0] * m for _ in range(m)]
        C_res = [[0] * m for _ in range(m)]
        
        for i in range(m):
            for k in range(m):
                for j in range(m):
                    T_res[i][k] = (T_res[i][k] + T_A[i][j] * T_B[j][k]) % MOD
                    C_res[i][k] = (C_res[i][k] + C_A[i][j] * T_B[j][k] + T_A[i][j] * C_B[j][k]) % MOD
        
        return (T_res, C_res)
    
    def build_matrix(c):
        T = [[0] * m for _ in range(m)]
        C = [[0] * m for _ in range(m)]
        
        for i in range(m):
            # Skip character c
            T[i][i] = 1
            
            # Include character c
            j = i
            while j > 0 and s[j] != c:
                j = fail[j-1]
            if s[j] == c:
                j += 1
            found = (j == m)
            if found:
                j = fail[m-1]
            
            T[i][j] = (T[i][j] + 1) % MOD
            if found:
                C[i][j] = (C[i][j] + 1) % MOD
        
        return (T, C)
    
    if x == 0:
        mat = build_matrix('0')
    elif x == 1:
        mat = build_matrix('1')
    else:
        mat_prev2 = build_matrix('0')
        mat_prev1 = build_matrix('1')
        for _ in range(2, x + 1):
            mat_curr = mat_mult(mat_prev1, mat_prev2)
            mat_prev2 = mat_prev1
            mat_prev1 = mat_curr
        mat = mat_prev1
    
    T, C = mat
    ans = sum(C[0][j] for j in range(m)) % MOD
    print(ans)

solve()
