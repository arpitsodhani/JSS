#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void add_implication_edge(int from, int to, int adj[2005][2005], int *deg) {
    adj[from][deg[from]++] = to;
}

void tarjan_dfs_scc(int u, int adj[2005][2005], int *deg, int *disc, int *low, int *on_stack, int *stack, int *top, int *scc_id, int *scc_count, int *time_counter) {
    disc[u] = low[u] = (*time_counter)++;
    stack[(*top)++] = u;
    on_stack[u] = 1;
    
    for (int i = 0; i < deg[u]; i++) {
        int v = adj[u][i];
        if (disc[v] == -1) {
            tarjan_dfs_scc(v, adj, deg, disc, low, on_stack, stack, top, scc_id, scc_count, time_counter);
            if (low[v] < low[u]) low[u] = low[v];
        } else if (on_stack[v] && disc[v] < low[u]) {
            low[u] = disc[v];
        }
    }
    
    if (low[u] == disc[u]) {
        while (1) {
            int v = stack[--(*top)];
            on_stack[v] = 0;
            scc_id[v] = *scc_count;
            if (v == u) break;
        }
        (*scc_count)++;
    }
}

int solve_2sat_instance(int n, int clauses[][2], int clause_count, int *assignment) {
    int adj[2005][2005], deg[2005] = {0};
    
    for (int i = 0; i < clause_count; i++) {
        int a = clauses[i][0];
        int b = clauses[i][1];
        int na = (a > 0) ? (2 * (a - 1) + 1) : (2 * (-a - 1));
        int nb = (b > 0) ? (2 * (b - 1)) : (2 * (-b - 1) + 1);
        int not_a = (a > 0) ? (2 * (a - 1)) : (2 * (-a - 1) + 1);
        int not_b = (b > 0) ? (2 * (b - 1) + 1) : (2 * (-b - 1));
        
        add_implication_edge(not_a, b > 0 ? 2*(b-1) : 2*(-b-1)+1, adj, deg);
        add_implication_edge(not_b, a > 0 ? 2*(a-1) : 2*(-a-1)+1, adj, deg);
    }
    
    int disc[2005], low[2005], on_stack[2005] = {0}, stack[2005], top = 0;
    int scc_id[2005], scc_count = 0, time_counter = 0;
    for (int i = 0; i < 2 * n; i++) disc[i] = low[i] = -1;
    
    for (int i = 0; i < 2 * n; i++) {
        if (disc[i] == -1) {
            tarjan_dfs_scc(i, adj, deg, disc, low, on_stack, stack, &top, scc_id, &scc_count, &time_counter);
        }
    }
    
    for (int i = 0; i < n; i++) {
        if (scc_id[2*i] == scc_id[2*i+1]) return 0;
        assignment[i] = scc_id[2*i] > scc_id[2*i+1];
    }
    return 1;
}

int main() {
    int n, m, clauses[1005][2], assignment[1005];
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; i++) {
        scanf("%d %d", &clauses[i][0], &clauses[i][1]);
    }
    
    if (solve_2sat_instance(n, clauses, m, assignment)) {
        for (int i = 0; i < n; i++) {
            printf("%d ", assignment[i]);
        }
    } else {
        printf("UNSATISFIABLE\n");
    }
    return 0;
}