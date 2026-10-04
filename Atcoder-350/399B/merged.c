#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, long long *a) {
scanf("%d", n); for(int i=0;i<*n;i++) scanf("%lld", &a[i]);
}

void compute_ranks(int n, long long *a, int *rank) {
long long *b=(long long*)malloc((size_t)n*sizeof(long long));
for(int i=0;i<n;i++) b[i]=a[i];
for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) if(b[j]>b[i]){ long long t=b[i]; b[i]=b[j]; b[j]=t; }
int r=1;
for(int i=0;i<n;){
  int j=i; while(j<n && b[j]==b[i]) j++;
  for(int k=i;k<j;k++){
    for(int p=0;p<n;p++) if(a[p]==b[i]) rank[p]=r;
  }
  r += (j-i);
  i=j;
}
free(b);
}

void print_ranks(int n, const int *rank) {
for(int i=0;i<n;i++) printf("%d\n", rank[i]);
}

int main(void){ int n; static long long a[105]; static int r[105]; read_input(&n,a); compute_ranks(n,a,r); print_ranks(n,r); return 0; }
