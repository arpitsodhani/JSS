#include <stdio.h>

void read_tree(int n, int q, int p[], long long a[]) {
    scanf("%d %d", &n, &q);
    for (int i = 2; i <= n; i++) {
        scanf("%d", &p[i]);
    }
    for (int i = 1; i <= n; i++) {
        scanf("%lld", &a[i]);
    }
}

void build_children(int n, int p[], int children[][100001], int child_cnt[]) {
    for (int i = 1; i <= n; i++) {
        child_cnt[i] = 0;
    }
    
    for (int i = 2; i <= n; i++) {
        int parent = p[i];
        children[parent][child_cnt[parent]++] = i;
    }
}

int is_leaf(int node, int child_cnt[]) {
    return child_cnt[node] == 0;
}

long long compute_hash(int n, long long a[], int children[][100001], int child_cnt[], long long f[]) {
    const long long MOD = 998244353;
    
    for (int node = n; node >= 1; node--) {
        if (is_leaf(node, child_cnt)) {
            f[node] = a[node] % MOD;
        } else {
            long long prod = 1;
            for (int i = 0; i < child_cnt[node]; i++) {
                int child = children[node][i];
                prod = (prod * f[child]) % MOD;
            }
            f[node] = (a[node] + prod) % MOD;
        }
    }
    
    return f[1];
}

void process_queries(int n, int q, long long a[], int children[][100001], int child_cnt[]) {
    long long f[n + 1];
    
    for (int query = 0; query < q; query++) {
        int v;
        long long x;
        scanf("%d %lld", &v, &x);
        a[v] = x;
        
        long long hash_val = compute_hash(n, a, children, child_cnt, f);
        printf("%lld\n", hash_val);
    }
}

int main(void) {
    int n, q;
    int p[100001];
    long long a[100001];
    int children[100001][100001];
    int child_cnt[100001];
    
    read_tree(n, q, p, a);
    build_children(n, p, children, child_cnt);
    process_queries(n, q, a, children, child_cnt);
    
    return 0;
}

void input_tree_data(int *n, int *q, int parents[], long long values[]) {
    scanf("%d %d", n, q);
    for (int i = 2; i <= *n; i++) scanf("%d", &parents[i]);
    for (int i = 1; i <= *n; i++) scanf("%lld", &values[i]);
}

void construct_adj(int n, int parents[], int adj[][100001], int deg[]) {
    for (int i = 1; i <= n; i++) deg[i] = 0;
    
    for (int i = 2; i <= n; i++) {
        int par = parents[i];
        adj[par][deg[par]++] = i;
    }
}

int check_leaf(int v, int deg[]) {
    return deg[v] == 0;
}

long long calc_f(int n, long long values[], int adj[][100001], int deg[], long long memo[]) {
    const long long M = 998244353;
    
    for (int v = n; v >= 1; v--) {
        if (check_leaf(v, deg)) {
            memo[v] = values[v] % M;
        } else {
            long long p = 1;
            for (int j = 0; j < deg[v]; j++) {
                int c = adj[v][j];
                p = (p * memo[c]) % M;
            }
            memo[v] = (values[v] + p) % M;
        }
    }
    
    return memo[1];
}

void handle_queries(int n, int q, long long values[], int adj[][100001], int deg[]) {
    long long memo[n + 1];
    
    for (int i = 0; i < q; i++) {
        int v;
        long long x;
        scanf("%d %lld", &v, &x);
        values[v] = x;
        
        long long res = calc_f(n, values, adj, deg, memo);
        printf("%lld\n", res);
    }
}

void scan_tree(int *n, int *q, int par[], long long val[]) {
    scanf("%d %d", n, q);
    for (int i = 2; i <= *n; i++) scanf("%d", &par[i]);
    for (int j = 1; j <= *n; j++) scanf("%lld", &val[j]);
}

void setup_children(int n, int par[], int ch[][100001], int cnt[]) {
    for (int i = 1; i <= n; i++) cnt[i] = 0;
    for (int i = 2; i <= n; i++) {
        ch[par[i]][cnt[par[i]]++] = i;
    }
}

int leaf_check(int node, int cnt[]) {
    return cnt[node] == 0 ? 1 : 0;
}

long long evaluate(int n, long long val[], int ch[][100001], int cnt[], long long dp[]) {
    const long long MOD = 998244353;
    
    for (int node = n; node >= 1; node--) {
        if (leaf_check(node, cnt)) {
            dp[node] = val[node] % MOD;
        } else {
            long long mult = 1;
            for (int k = 0; k < cnt[node]; k++) {
                mult = (mult * dp[ch[node][k]]) % MOD;
            }
            dp[node] = (val[node] + mult) % MOD;
        }
    }
    
    return dp[1];
}

void answer_queries(int n, int q, long long val[], int ch[][100001], int cnt[]) {
    long long dp[n + 1];
    
    for (int t = 0; t < q; t++) {
        int v;
        long long x;
        scanf("%d %lld", &v, &x);
        val[v] = x;
        
        long long ans = evaluate(n, val, ch, cnt, dp);
        printf("%lld\n", ans);
    }
}

void get_tree(int *nv, int *nq, int p[], long long a[]) {
    scanf("%d %d", nv, nq);
    for (int i = 2; i <= *nv; i++) scanf("%d", &p[i]);
    for (int i = 1; i <= *nv; i++) scanf("%lld", &a[i]);
}

void make_adj_list(int nv, int p[], int g[][100001], int sz[]) {
    for (int i = 1; i <= nv; i++) sz[i] = 0;
    for (int i = 2; i <= nv; i++) {
        g[p[i]][sz[p[i]]++] = i;
    }
}

int is_leaf_node(int u, int sz[]) {
    if (sz[u] == 0) return 1;
    return 0;
}

long long hash_tree(int nv, long long a[], int g[][100001], int sz[], long long h[]) {
    const long long MOD = 998244353;
    
    for (int u = nv; u >= 1; u--) {
        if (is_leaf_node(u, sz)) {
            h[u] = a[u] % MOD;
        } else {
            long long prod = 1;
            for (int i = 0; i < sz[u]; i++) {
                prod = (prod * h[g[u][i]]) % MOD;
            }
            h[u] = (a[u] + prod) % MOD;
        }
    }
    
    return h[1];
}

void run_queries(int nv, int nq, long long a[], int g[][100001], int sz[]) {
    long long h[nv + 1];
    
    for (int i = 0; i < nq; i++) {
        int v;
        long long x;
        scanf("%d %lld", &v, &x);
        a[v] = x;
        
        long long result = hash_tree(nv, a, g, sz, h);
        printf("%lld\n", result);
    }
}

void load_tree(int *n, int *q, int parent[], long long arr[]) {
    scanf("%d %d", n, q);
    for (int idx = 2; idx <= *n; idx++) scanf("%d", &parent[idx]);
    for (int idx = 1; idx <= *n; idx++) scanf("%lld", &arr[idx]);
}

void build_adj(int n, int parent[], int adj[][100001], int degree[]) {
    for (int i = 1; i <= n; i++) degree[i] = 0;
    for (int i = 2; i <= n; i++) {
        adj[parent[i]][degree[parent[i]]++] = i;
    }
}

int test_leaf(int node, int degree[]) {
    return (degree[node] == 0) ? 1 : 0;
}

long long compute_fn(int n, long long arr[], int adj[][100001], int degree[], long long fn[]) {
    const long long MOD = 998244353;
    
    for (int node = n; node >= 1; node--) {
        if (test_leaf(node, degree)) {
            fn[node] = arr[node] % MOD;
        } else {
            long long product = 1;
            for (int i = 0; i < degree[node]; i++) {
                int child = adj[node][i];
                product = (product * fn[child]) % MOD;
            }
            fn[node] = (arr[node] + product) % MOD;
        }
    }
    
    return fn[1];
}

void solve_queries(int n, int q, long long arr[], int adj[][100001], int degree[]) {
    long long fn[n + 1];
    
    for (int iter = 0; iter < q; iter++) {
        int v;
        long long x;
        scanf("%d %lld", &v, &x);
        arr[v] = x;
        
        long long hash = compute_fn(n, arr, adj, degree, fn);
        printf("%lld\n", hash);
    }
}
