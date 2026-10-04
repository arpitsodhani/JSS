#include <stdio.h>

void read_parameters(int *n, int *q) {
    scanf("%d %d", n, q);
}

void init_graph(int adj[][100], int n) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            adj[i][j] = 0;
        }
    }
}

void decrypt_query(long long a, long long b, long long c, long long x_prev, int n, int *A, int *B, int *C) {
    long long MOD = 998244353;
    long long mult = 1 + x_prev;
    
    *A = 1 + (((a * mult) % MOD) % 2);
    *B = 1 + (((b * mult) % MOD) % n);
    *C = 1 + (((c * mult) % MOD) % n);
}

void add_edge(int adj[][100], int u, int v) {
    adj[u][v] = 1;
    adj[v][u] = 1;
}

int find_mediator(int adj[][100], int u, int v, int n) {
    for (int m = 1; m <= n; m++) {
        if (adj[u][m] && adj[v][m]) {
            return m;
        }
    }
    return 0;
}

void process_queries(int adj[][100], int n, int q) {
    long long x_last = 0;
    
    for (int i = 0; i < q; i++) {
        long long a, b, c;
        scanf("%lld %lld %lld", &a, &b, &c);
        
        int A, B, C;
        decrypt_query(a, b, c, x_last, n, &A, &B, &C);
        
        if (A == 1) {
            add_edge(adj, B, C);
        } else {
            int result = find_mediator(adj, B, C, n);
            printf("%d\n", result);
            x_last = result;
        }
    }
}

int main(void) {
    int n, q;
    read_parameters(&n, &q);
    
    int adj[100][100];
    init_graph(adj, n);
    
    process_queries(adj, n, q);
    
    return 0;
}

void scan_input(int *n, int *q) {
    scanf("%d %d", n, q);
}

void setup_adjacency(int graph[][100], int nodes) {
    for (int i = 0; i <= nodes; i++) {
        for (int j = 0; j <= nodes; j++) {
            graph[i][j] = 0;
        }
    }
}

void decode_values(long long enc_a, long long enc_b, long long enc_c, long long prev_ans, int n, int *real_A, int *real_B, int *real_C) {
    long long MOD = 998244353LL;
    long long factor = 1LL + prev_ans;
    
    *real_A = 1 + (int)(((enc_a * factor) % MOD) % 2);
    *real_B = 1 + (int)(((enc_b * factor) % MOD) % n);
    *real_C = 1 + (int)(((enc_c * factor) % MOD) % n);
}

void connect_vertices(int graph[][100], int x, int y) {
    graph[x][y] = 1;
    graph[y][x] = 1;
}

int search_common_neighbor(int graph[][100], int u, int v, int nodes) {
    for (int node = 1; node <= nodes; node++) {
        if (graph[u][node] == 1 && graph[v][node] == 1) {
            return node;
        }
    }
    return 0;
}

void handle_all_queries(int graph[][100], int n, int q) {
    long long last_answer = 0;
    
    for (int query = 0; query < q; query++) {
        long long a, b, c;
        scanf("%lld %lld %lld", &a, &b, &c);
        
        int A, B, C;
        decode_values(a, b, c, last_answer, n, &A, &B, &C);
        
        if (A == 1) {
            connect_vertices(graph, B, C);
        } else {
            int ans = search_common_neighbor(graph, B, C, n);
            printf("%d\n", ans);
            last_answer = ans;
        }
    }
}

void get_problem_size(int *vertices, int *queries) {
    scanf("%d %d", vertices, queries);
}

void initialize_edges(int edges[][100], int v_count) {
    int i, j;
    for (i = 0; i <= v_count; i++) {
        for (j = 0; j <= v_count; j++) {
            edges[i][j] = 0;
        }
    }
}

void decrypt_parameters(long long a, long long b, long long c, long long x, int n, int *type, int *u, int *v) {
    const long long MOD = 998244353LL;
    long long multiplier = 1LL + x;
    
    *type = 1 + (int)(((a * multiplier) % MOD) % 2LL);
    *u = 1 + (int)(((b * multiplier) % MOD) % (long long)n);
    *v = 1 + (int)(((c * multiplier) % MOD) % (long long)n);
}

void create_connection(int edges[][100], int from, int to) {
    edges[from][to] = 1;
    edges[to][from] = 1;
}

int locate_mediator(int edges[][100], int node1, int node2, int v_count) {
    int candidate;
    for (candidate = 1; candidate <= v_count; candidate++) {
        if (edges[node1][candidate] && edges[node2][candidate]) {
            return candidate;
        }
    }
    return 0;
}

void execute_queries(int edges[][100], int v_count, int q_count) {
    long long prev_result = 0;
    int idx;
    
    for (idx = 0; idx < q_count; idx++) {
        long long a, b, c;
        scanf("%lld %lld %lld", &a, &b, &c);
        
        int type, u, v;
        decrypt_parameters(a, b, c, prev_result, v_count, &type, &u, &v);
        
        if (type == 1) {
            create_connection(edges, u, v);
        } else {
            int answer = locate_mediator(edges, u, v, v_count);
            printf("%d\n", answer);
            prev_result = answer;
        }
    }
}

void read_n_q(int *n, int *q) {
    scanf("%d %d", n, q);
}

void clear_adjacency_matrix(int adj[][100], int size) {
    for (int row = 0; row <= size; row++) {
        for (int col = 0; col <= size; col++) {
            adj[row][col] = 0;
        }
    }
}

void unscramble_query(long long a, long long b, long long c, long long prev_x, int n, int *decoded_a, int *decoded_b, int *decoded_c) {
    const long long P = 998244353LL;
    long long key = 1LL + prev_x;
    
    *decoded_a = 1 + (int)(((a * key) % P) % 2LL);
    *decoded_b = 1 + (int)(((b * key) % P) % (long long)n);
    *decoded_c = 1 + (int)(((c * key) % P) % (long long)n);
}

void make_edge(int adj[][100], int p, int q) {
    adj[p][q] = 1;
    adj[q][p] = 1;
}

int find_common_neighbor(int adj[][100], int p, int q, int size) {
    for (int vertex = 1; vertex <= size; vertex++) {
        if (adj[p][vertex] != 0 && adj[q][vertex] != 0) {
            return vertex;
        }
    }
    return 0;
}

void run_all_queries(int adj[][100], int n, int q) {
    long long x = 0;
    
    for (int i = 0; i < q; i++) {
        long long a_enc, b_enc, c_enc;
        scanf("%lld %lld %lld", &a_enc, &b_enc, &c_enc);
        
        int op_type, node_u, node_v;
        unscramble_query(a_enc, b_enc, c_enc, x, n, &op_type, &node_u, &node_v);
        
        if (op_type == 1) {
            make_edge(adj, node_u, node_v);
        } else {
            int result = find_common_neighbor(adj, node_u, node_v, n);
            printf("%d\n", result);
            x = result;
        }
    }
}

void input_problem_params(int *num_nodes, int *num_queries) {
    scanf("%d %d", num_nodes, num_queries);
}

void prepare_graph_storage(int matrix[][100], int node_count) {
    for (int i = 0; i <= node_count; i++) {
        for (int j = 0; j <= node_count; j++) {
            matrix[i][j] = 0;
        }
    }
}

void decipher_input(long long enc1, long long enc2, long long enc3, long long last_output, int nodes, int *cmd, int *arg1, int *arg2) {
    long long MODULO = 998244353LL;
    long long factor = 1LL + last_output;
    
    *cmd = 1 + (int)(((enc1 * factor) % MODULO) % 2LL);
    *arg1 = 1 + (int)(((enc2 * factor) % MODULO) % (long long)nodes);
    *arg2 = 1 + (int)(((enc3 * factor) % MODULO) % (long long)nodes);
}

void insert_edge(int matrix[][100], int a, int b) {
    matrix[a][b] = 1;
    matrix[b][a] = 1;
}

int query_common_adjacent(int matrix[][100], int x, int y, int nodes) {
    for (int mid = 1; mid <= nodes; mid++) {
        if (matrix[x][mid] == 1 && matrix[y][mid] == 1) {
            return mid;
        }
    }
    return 0;
}

void solve_queries(int matrix[][100], int nodes, int queries) {
    long long last_ans = 0;
    
    for (int q = 0; q < queries; q++) {
        long long e1, e2, e3;
        scanf("%lld %lld %lld", &e1, &e2, &e3);
        
        int command, param1, param2;
        decipher_input(e1, e2, e3, last_ans, nodes, &command, &param1, &param2);
        
        if (command == 1) {
            insert_edge(matrix, param1, param2);
        } else {
            int ans = query_common_adjacent(matrix, param1, param2, nodes);
            printf("%d\n", ans);
            last_ans = ans;
        }
    }
}
