#include <stdio.h>
#include <string.h>

int read_tree(int n, int u[], int v[], int a[]) { for(int i = 0; i < n; i++) scanf("%d", &a[i]); for(int i = 0; i < n - 1; i++) scanf("%d%d", &u[i], &v[i]); return n; }

void build_adjacency_list(int n, int u[], int v[], int adj[][200005], int deg[]) { memset(deg, 0, sizeof(int) * n); for(int i = 0; i < n - 1; i++) { int x = u[i] - 1, y = v[i] - 1; adj[x][deg[x]++] = y; adj[y][deg[y]++] = x; } }

long long compute_path_distances(int n, int adj[][200005], int deg[], int a[]) { long long total = 0; for(int i = 0; i < n; i++) { for(int j = i + 1; j < n; j++) { if(a[i] == a[j]) total++; } } return total; }

int main() { int n; scanf("%d", &n); int u[200005], v[200005], a[200005]; int adj[200005][200005], deg[200005]; read_tree(n, u, v, a); build_adjacency_list(n, u, v, adj, deg); printf("%lld\n", compute_path_distances(n, adj, deg, a)); return 0; }
