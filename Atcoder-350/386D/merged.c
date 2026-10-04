#include <stdio.h>

void read_input(int *N,int *M,int *X,int *Y,char *C) {
scanf("%d%d", N,M); for(int i=0;i<*M;i++) scanf("%d%d %c", &X[i], &Y[i], &C[i]);
}

int possible(int N,int M,int *X,int *Y,char *C) {
static int L[200005], U[200005];
for(int i=1;i<=N;i++){ L[i]=0; U[i]=N; }
for(int i=0;i<M;i++){
  int r=X[i], c=Y[i]; if(C[i]=='B'){ if(c>L[r]) L[r]=c; } else { if(c-1<U[r]) U[r]=c-1; }
}
int prev=N; for(int i=1;i<=N;i++){
  if(L[i]>U[i]) return 0; int ri=U[i]; if(ri>prev) ri=prev; if(ri<L[i]) return 0; prev=ri; }
return 1;
}

void print_yesno(int x) {
printf("%s\n", x?"Yes":"No");
}

int main(void){ int N,M; static int X[200005],Y[200005]; static char C[200005]; read_input(&N,&M,X,Y,C); int ok=possible(N,M,X,Y,C); print_yesno(ok); return 0;}
