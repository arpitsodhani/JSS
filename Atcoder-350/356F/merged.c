#include <stdio.h>

long long find_kth_distance(long long set[], int size, long long x, long long k) { long long dists[200005]; int cnt = 0; for(int i = 0; i < size; i++) { if(set[i] == x) continue; long long d = set[i] > x ? set[i] - x : x - set[i]; dists[cnt++] = d; } for(int i = 0; i < cnt - 1; i++) for(int j = i + 1; j < cnt; j++) if(dists[i] > dists[j]) { long long t = dists[i]; dists[i] = dists[j]; dists[j] = t; } return dists[k-1]; }

int main() { long long k; int q = read_input(&k); long long set[200005]; int size = 0; for(int i = 0; i < q; i++) { int type; long long x; scanf("%d%lld", &type, &x); if(type == 1) toggle_element(set, &size, x); else printf("%lld\n", find_kth_distance(set, size, x, k)); } return 0; }

int read_input(long long *k) { int q; scanf("%d%lld", &q, k); return q; }

void toggle_element(long long set[], int *size, long long x) { int found = -1; for(int i = 0; i < *size; i++) if(set[i] == x) { found = i; break; } if(found >= 0) { for(int i = found; i < *size - 1; i++) set[i] = set[i+1]; (*size)--; } else { set[(*size)++] = x; } }

