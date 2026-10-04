#include <stdio.h>

int read_q(int *N) {
int Q; scanf("%d%d", N,&Q); return Q;
}

void process(int N,int Q) {
static int pos[200005],cnt[200005];
for(int i=1;i<=N;i++){ pos[i]=i; cnt[i]=1; }
int over=0;
for(int qi=0;qi<Q;qi++){
  int t; scanf("%d", &t);
  if(t==1){ int P,H; scanf("%d%d", &P,&H); int old=pos[P];
    if(cnt[old]==2) over--; cnt[old]--; if(cnt[old]==2) over++; if(cnt[old]<2) {}
    if(cnt[H]==1) over++; cnt[H]++; pos[P]=H;
  } else {
    printf("%d\n", over);
  }
}
}

int main(void){ int N; int Q=read_q(&N); process(N,Q); return 0;}
