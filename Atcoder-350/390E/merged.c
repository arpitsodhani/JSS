#include <stdio.h>
#include <stdlib.h>

void read_input(int *n,int *X,int *V,int *A,int *C) {
scanf("%d%d", n,X); for(int i=0;i<*n;i++) scanf("%d%d%d", &V[i], &A[i], &C[i]);
}

int max_min(int n,int X,int *V,int *A,int *C) {
int *dp1=(int*)calloc((size_t)(X+1),sizeof(int));
int *dp2=(int*)calloc((size_t)(X+1),sizeof(int));
int *dp3=(int*)calloc((size_t)(X+1),sizeof(int));
for(int i=0;i<n;i++){
  for(int x=X; x>=C[i]; x--){
    if(V[i]==1 && dp1[x-C[i]]+A[i]>dp1[x]) dp1[x]=dp1[x-C[i]]+A[i];
    if(V[i]==2 && dp2[x-C[i]]+A[i]>dp2[x]) dp2[x]=dp2[x-C[i]]+A[i];
    if(V[i]==3 && dp3[x-C[i]]+A[i]>dp3[x]) dp3[x]=dp3[x-C[i]]+A[i];
  }
}
int best=0; for(int x=0;x<=X;x++){ int m=dp1[x]; if(dp2[x]<m) m=dp2[x]; if(dp3[x]<m) m=dp3[x]; if(m>best) best=m; }
free(dp1); free(dp2); free(dp3); return best;
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ int n,X; static int V[205],A[205],C[205]; read_input(&n,&X,V,A,C); int ans=max_min(n,X,V,A,C); print_int(ans); return 0;}
