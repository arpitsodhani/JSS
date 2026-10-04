#include <stdio.h>
#include <stdlib.h>

void read_input(int *n,int *m,int *U,int *V) {
scanf("%d%d", n,m); for(int i=0;i<*m;i++) scanf("%d%d", &U[i], &V[i]);
}

long long count_remove(int m,int *U,int *V) {
long long ans=0;
typedef struct{int a,b;} P;
P *arr=(P*)malloc((size_t)m*sizeof(P));
for(int i=0;i<m;i++){ int a=U[i], b=V[i]; if(a==b) ans++; else { if(a>b){int t=a;a=b;b=t;} arr[i].a=a; arr[i].b=b; } }
for(int i=0;i<m;i++) for(int j=i+1;j<m;j++){
  if(arr[i].a==0||arr[j].a==0) continue;
  if(arr[i].a==arr[j].a && arr[i].b==arr[j].b){ ans++; arr[j].a=0; arr[j].b=0; }
}
free(arr); return ans;
}

void print_ll(long long x) {
printf("%lld\n", x);
}

int main(void){ int n,m; static int U[200005],V[200005]; read_input(&n,&m,U,V); long long ans=count_remove(m,U,V); print_ll(ans); return 0; }
