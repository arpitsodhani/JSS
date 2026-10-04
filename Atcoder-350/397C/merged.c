#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, int *a) {
scanf("%d", n); for(int i=0;i<*n;i++) scanf("%d", &a[i]);
}

void build_pref(int n, const int *a, int *pref) {
int *seen=(int*)calloc((size_t)(n+1),sizeof(int));
int c=0;
for(int i=0;i<n;i++){
  int x=a[i];
  if(!seen[x]){ seen[x]=1; c++; }
  pref[i]=c;
}
free(seen);
}

void build_suf(int n, const int *a, int *suf) {
int *seen=(int*)calloc((size_t)(n+1),sizeof(int));
int c=0;
for(int i=n-1;i>=0;i--){
  int x=a[i];
  if(!seen[x]){ seen[x]=1; c++; }
  suf[i]=c;
}
free(seen);
}

int max_split(int n, const int *pref, const int *suf) {
int best=0;
for(int i=0;i<n-1;i++){
  int v=pref[i]+suf[i+1];
  if(v>best) best=v;
}
return best;
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ int n; int *a=(int*)malloc((size_t)300000*sizeof(int)); read_input(&n,a); int *pref=(int*)malloc((size_t)n*sizeof(int)); int *suf=(int*)malloc((size_t)n*sizeof(int)); build_pref(n,a,pref); build_suf(n,a,suf); int ans=max_split(n,pref,suf); print_int(ans); free(a); free(pref); free(suf); return 0; }
