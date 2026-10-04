#include <stdio.h>
#include <string.h>

int read_graph(int next[]) { int n; scanf("%d", &n); for(int i = 1; i <= n; i++) scanf("%d", &next[i]); return n; }

int find_cycle(int start, int next[], int visited[], int cycle_nodes[]) { int current = start; while(!visited[current]) { visited[current] = 1; current = next[current]; } int cycle_start = current; int cycle_size = 0; do { cycle_nodes[current] = 1; cycle_size++; current = next[current]; } while(current != cycle_start); return cycle_size; }

long long count_reachable_from(int start, int next[], int visited[], int cycle_nodes[]) { long long count = 0; int current = start; while(!visited[current]) { visited[current] = 1; count++; current = next[current]; } if(cycle_nodes[current]) { int cycle_start = current; do { count++; current = next[current]; } while(current != cycle_start); } return count; }

long long compute_total_pairs(int n, int next[]) { long long total = 0; for(int u = 1; u <= n; u++) { int visited[200005] = {0}; int cycle_nodes[200005] = {0}; find_cycle(u, next, visited, cycle_nodes); memset(visited, 0, sizeof(visited)); total += count_reachable_from(u, next, visited, cycle_nodes); } return total; }

int main() { int next[200005]; int n = read_graph(next); printf("%lld\n", compute_total_pairs(n, next)); return 0; }
