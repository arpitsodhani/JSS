#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, int *x, int *a) {
scanf("%d %d", n, x); for(int i=0;i<*n;i++) scanf("%d", &a[i]);
}

int cmp_int(const void *p, const void *q) {
int x=*(const int*)p, y=*(const int*)q; return (x>y)-(x<y);
}

long long sum_smallest(int n, int x, int *a) {
qsort(a,(size_t)n,sizeof(int),cmp_int); long long s=0; for(int i=0;i<x;i++) s+=a[i]; return s;
}

void print_ll(long long v) {
printf("%lld\n", v);
}

int main(void){ int n,x; static int a[105]; read_input(&n,&x,a); long long ans=sum_smallest(n,x,a); print_ll(ans); return 0; }
