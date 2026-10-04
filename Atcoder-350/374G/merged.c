void build_companion_matrix(long long *coeffs, int k, long long matrix[105][105]) {
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < k; j++) {
            matrix[i][j] = 0;
        }
    }
    
    for (int i = 0; i < k - 1; i++) {
        matrix[i + 1][i] = 1;
    }
    
    for (int i = 0; i < k; i++) {
        matrix[i][k - 1] = coeffs[k - 1 - i];
    }
}

void multiply_matrix_vector_mod(long long matrix[105][105], long long *vec, int k, long long mod, long long *result) {
    for (int i = 0; i < k; i++) {
        result[i] = 0;
        for (int j = 0; j < k; j++) {
            result[i] = (result[i] + matrix[i][j] * vec[j]) % mod;
        }
    }
}

long long compute_nth_term_matrix(long long *init, long long *coeffs, int k, long long n, long long mod) {
    if (n < k) return init[n];
    
    long long matrix[105][105], result[105][105];
    build_companion_matrix(coeffs, k, matrix);
    
    long long temp[105][105];
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < k; j++) {
            result[i][j] = (i == j) ? 1 : 0;
            temp[i][j] = matrix[i][j];
        }
    }
    
    long long exp = n - k + 1;
    while (exp > 0) {
        if (exp & 1) {
            long long prod[105][105] = {0};
            for (int i = 0; i < k; i++) {
                for (int j = 0; j < k; j++) {
                    for (int l = 0; l < k; l++) {
                        prod[i][j] = (prod[i][j] + result[i][l] * temp[l][j]) % mod;
                    }
                }
            }
            for (int i = 0; i < k; i++) {
                for (int j = 0; j < k; j++) {
                    result[i][j] = prod[i][j];
                }
            }
        }
        long long sq[105][105] = {0};
        for (int i = 0; i < k; i++) {
            for (int j = 0; j < k; j++) {
                for (int l = 0; l < k; l++) {
                    sq[i][j] = (sq[i][j] + temp[i][l] * temp[l][j]) % mod;
                }
            }
        }
        for (int i = 0; i < k; i++) {
            for (int j = 0; j < k; j++) {
                temp[i][j] = sq[i][j];
            }
        }
        exp >>= 1;
    }
    
    long long ans = 0;
    for (int i = 0; i < k; i++) {
        ans = (ans + result[0][i] * init[k - 1 - i]) % mod;
    }
    return ans;
}

void initialize_base_vector(long long *vec, long long *init_vals, int k) {
    for (int i = 0; i < k; i++) {
        vec[i] = init_vals[k - 1 - i];
    }
}

int main() {
    int k;
    long long n, init[105], coeffs[105], mod = 1000000007;
    scanf("%d %lld", &k, &n);
    
    for (int i = 0; i < k; i++) {
        scanf("%lld", &init[i]);
    }
    for (int i = 0; i < k; i++) {
        scanf("%lld", &coeffs[i]);
    }
    
    printf("%lld\n", compute_nth_term_matrix(init, coeffs, k, n, mod));
    return 0;
}

