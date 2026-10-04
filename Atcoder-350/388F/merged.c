#include <stdio.h>

void read_input(int *n,int *A,int *B,int *m,int *L,int *R) {
scanf("%d%d%d%d", n,A,B,m); for(int i=0;i<*m;i++) scanf("%d%d", &L[i], &R[i]);
}

int can_reach(int n,int A,int B,int m,int *L,int *R) {
int bad[105]={0};
for(int i=0;i<m;i++) for(int j=L[i];j<=R[i];j++) bad[j]=1;
int q[1000],qh=0,qt=0,vis[105]={0};
if(bad[1]) return 0; q[qt++]=1; vis[1]=1;
while(qh<qt){
  int x=q[qh++]; if(x==n) return 1;
  for(int d=A; d<=B; d++){
    int y=x+d; if(y<1||y>n) continue; if(bad[y]) continue; if(!vis[y]){vis[y]=1; q[qt++]=y;}
  }
}
return 0;
}

void print_yesno(int x) {
printf("%s\n", x?"Yes":"No");
}

int main(void){ int n,A,B,m; int L[205],R[205]; read_input(&n,&A,&B,&m,L,R); int ok=can_reach(n,A,B,m,L,R); print_yesno(ok); return 0;}
