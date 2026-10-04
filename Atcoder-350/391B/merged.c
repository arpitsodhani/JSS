#include <stdio.h>

void read_input(int *N,int *M,char S[][105],char T[][105]) {
scanf("%d%d", N,M); for(int i=0;i<*N;i++) scanf("%s", S[i]); for(int i=0;i<*M;i++) scanf("%s", T[i]);
}

void find_pos(int N,int M,char S[][105],char T[][105],int *a,int *b) {
for(int i=0;i+M<=N;i++) for(int j=0;j+M<=N;j++){
  int ok=1; for(int x=0;x<M;x++) for(int y=0;y<M;y++) if(S[i+x][j+y]!=T[x][y]) ok=0;
  if(ok){ *a=i+1; *b=j+1; return; }
}
*a=1; *b=1;
}

void print_pos(int a,int b) {
printf("%d %d\n", a,b);
}

int main(void){ int N,M; char S[105][105],T[105][105]; read_input(&N,&M,S,T); int a,b; find_pos(N,M,S,T,&a,&b); print_pos(a,b); return 0;}
