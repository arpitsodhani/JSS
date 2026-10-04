#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, int *a) {
scanf("%d", n); for(int i=0;i<*n;i++) scanf("%d", &a[i]);
}

int shortest_dup(int n, const int *a) {
int *last=(int*)malloc((size_t)1000005*sizeof(int));
for(int i=0;i<=1000000;i++) last[i]=-1;
int ans=1e9;
for(int i=0;i<n;i++){
  int x=a[i];
  if(last[x]!=-1){
    int len=i-last[x]+1;
    if(len<ans) ans=len;
  }
  last[x]=i;
}
free(last);
if(ans==1e9) return -1;
return ans;
}

int main(void){ int n; static int a[200005]; read_input(&n,a); int ans=shortest_dup(n,a); printf("%d\n", ans); return 0; }
