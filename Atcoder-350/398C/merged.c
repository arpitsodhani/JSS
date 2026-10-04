#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, int *a) {
scanf("%d", n); for(int i=0;i<*n;i++) scanf("%d", &a[i]);
}

int find_unique_max(int n, const int *a) {
int *cnt=(int*)calloc((size_t)(n+1), sizeof(int));
for(int i=0;i<n;i++) cnt[a[i]]++;
int best=-1;
for(int i=0;i<n;i++) if(cnt[a[i]]==1){ if(best==-1||a[i]>a[best]) best=i; }
free(cnt);
return (best==-1)?-1:(best+1);
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ int n; int *a=(int*)malloc((size_t)200000*sizeof(int)); read_input(&n,a); int ans=find_unique_max(n,a); print_int(ans); free(a); return 0; }
