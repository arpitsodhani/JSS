long long modular_power_fast(long long base, long long exp, long long mod) {
    long long result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % mod;
        base = (base * base) % mod;
        exp >>= 1;
    }
    return result;
}

void insert_hash_entry(long long key, long long value, long long *keys, long long *values, int *hash_table, int table_size) {
    int idx = key % table_size;
    while (hash_table[idx] != -1) {
        idx = (idx + 1) % table_size;
    }
    hash_table[idx] = 1;
    keys[idx] = key;
    values[idx] = value;
}

long long search_hash_entry(long long key, long long *keys, long long *values, int *hash_table, int table_size) {
    int idx = key % table_size;
    while (hash_table[idx] != -1) {
        if (keys[idx] == key) return values[idx];
        idx = (idx + 1) % table_size;
    }
    return -1;
}

long long discrete_log_baby_giant(long long a, long long b, long long p) {
    long long m = (long long)ceil(sqrt(p));
    long long keys[100005], values[100005];
    int hash_table[100005];
    for (int i = 0; i < 100005; i++) hash_table[i] = -1;
    
    long long gamma = 1;
    for (long long j = 0; j < m; j++) {
        insert_hash_entry(gamma, j, keys, values, hash_table, 100005);
        gamma = (gamma * a) % p;
    }
    
    long long factor = modular_power_fast(a, m * (p - 2), p);
    long long cur = b;
    
    for (long long i = 0; i < m; i++) {
        long long j = search_hash_entry(cur, keys, values, hash_table, 100005);
        if (j != -1) return i * m + j;
        cur = (cur * factor) % p;
    }
    return -1;
}

int main() {
    long long a, b, p;
    scanf("%lld %lld %lld", &a, &b, &p);
    long long result = discrete_log_baby_giant(a, b, p);
    if (result == -1) {
        printf("No solution\n");
    } else {
        printf("%lld\n", result);
    }
    return 0;
}

