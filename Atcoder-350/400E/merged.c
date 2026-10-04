#include <stdio.h>
#include <stdlib.h>

int* build_factor_counts(int A) {
int *v=(int*)calloc((size_t)A, sizeof(int));
for(int p=2;p<A;p++) if(v[p]==0) for(int j=p;j<A;j+=p) v[j]++; return v;
}

long long* build_400_numbers(const int *v, int A, int *out_n) {
long long *tmp=(long long*)malloc((size_t)A*sizeof(long long)); int cnt=0; for(long long i=2;i<A;i++) if(v[i]==2) tmp[cnt++]=i*i; *out_n=cnt; return (long long*)realloc(tmp,(size_t)cnt*sizeof(long long));
}

long long answer_query(const long long *arr, int n, long long a) {
int l=0,r=n; while(l<r){ int m=(l+r)/2; if(arr[m]<=a) l=m+1; else r=m; } return arr[l-1];
}

int main(void){ int A=1000001; int *v=build_factor_counts(A); int n; long long *arr=build_400_numbers(v,A,&n); free(v); int q; scanf("%d", &q); while(q--){ long long a; scanf("%lld", &a); long long ans=answer_query(arr,n,a); printf("%lld\n", ans); } free(arr); return 0; }
