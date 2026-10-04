#include <stdio.h>

void read_input(int *n,int *m,int *a) {
scanf("%d%d", n,m); for(int i=0;i<*m;i++) scanf("%d", &a[i]);
}

void mark_missing(int n,int m,int *a,int *used) {
for(int i=0;i<=n;i++) used[i]=0; for(int i=0;i<m;i++) used[a[i]]=1;
}

void print_missing(int n,int *used) {
for(int i=1;i<=n;i++) if(!used[i]) printf("%d ", i); printf("\n");
}

int main(void){ int n,m; int a[105]; int used[105]; read_input(&n,&m,a); mark_missing(n,m,a,used); print_missing(n,used); return 0; }
