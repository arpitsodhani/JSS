#include <stdio.h>
#include <stdlib.h>

void read_case(int *n, int *a) {
scanf("%d", n); for(int i=0;i<2*(*n);i++){ scanf("%d", &a[i]); a[i]--; }
}

long long solve_case(int n, const int *a) {
int N=n;
int *p1=(int*)malloc((size_t)N*sizeof(int));
int *p2=(int*)malloc((size_t)N*sizeof(int));
for(int i=0;i<N;i++){ p1[i]=-1; p2[i]=-1; }
for(int i=0;i<2*N;i++){
  int x=a[i];
  if(p1[x]==-1) p1[x]=i; else p2[x]=i;
}
char *adj=(char*)calloc((size_t)N*(size_t)N,1);
for(int x=0;x<N;x++){
  if(p2[x]==p1[x]+1) continue;
  for(int y=x+1;y<N;y++){
    if(p2[y]==p1[y]+1) continue;
    int a1=p1[x], a2=p2[x], b1=p1[y], b2=p2[y];
    if(a1>a2){ int t=a1;a1=a2;a2=t; }
    if(b1>b2){ int t=b1;b1=b2;b2=t; }
    int ok=0;
    if(abs(a1-b1)==1 && abs(a2-b2)==1) ok=1;
    if(ok) adj[x*N+y]=1;
  }
}
long long ans=0;
for(int i=0;i<N;i++) for(int j=i+1;j<N;j++) if(adj[i*N+j]) ans++;
free(p1); free(p2); free(adj);
return ans;
}

int main(void){ int T; scanf("%d", &T); while(T--){ int n; int *a=(int*)malloc((size_t)400000*sizeof(int)); read_case(&n,a); long long ans=solve_case(n,a); printf("%lld\n", ans); free(a); } return 0; }
