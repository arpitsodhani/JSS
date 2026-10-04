void multiply_matrices_mod(long long a[105][105], long long b[105][105], int n, long long mod, long long result[105][105]) {
    long long temp[105][105] = {0};
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                temp[i][j] = (temp[i][j] + a[i][k] * b[k][j]) % mod;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            result[i][j] = temp[i][j];
        }
    }
}

void initialize_identity_matrix(long long matrix[105][105], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            matrix[i][j] = (i == j) ? 1 : 0;
        }
    }
}

void matrix_power_binary(long long base[105][105], long long exp, int n, long long mod, long long result[105][105]) {
    long long temp[105][105];
    initialize_identity_matrix(result, n);
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            temp[i][j] = base[i][j];
        }
    }
    
    while (exp > 0) {
        if (exp & 1) {
            long long prod[105][105];
            multiply_matrices_mod(result, temp, n, mod, prod);
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    result[i][j] = prod[i][j];
                }
            }
        }
        long long sq[105][105];
        multiply_matrices_mod(temp, temp, n, mod, sq);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                temp[i][j] = sq[i][j];
            }
        }
        exp >>= 1;
    }
}

void copy_matrix(long long src[][105], long long dst[][105], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dst[i][j] = src[i][j];
        }
    }
}

int main() {
    int n;
    long long exp, matrix[105][105], result[105][105], mod = 1000000007;
    scanf("%d %lld", &n, &exp);
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%lld", &matrix[i][j]);
        }
    }
    
    matrix_power_binary(matrix, exp, n, mod, result);
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%lld ", result[i][j]);
        }
        printf("\n");
    }
    return 0;
}

