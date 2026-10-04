#include <stdio.h>

void read_input(int *a,int *b,int *c,int *d) {
scanf("%d%d%d%d", a,b,c,d);
}

int can_full(int a,int b,int c,int d) {
int cnt[14]={0}; cnt[a]++; cnt[b]++; cnt[c]++; cnt[d]++;
for(int x=1;x<=13;x++){
  cnt[x]++; int three=0,two=0; for(int v=1;v<=13;v++){ if(cnt[v]==3) three++; if(cnt[v]==2) two++; }
  cnt[x]--; if(three==1 && two==1) return 1;
}
return 0;
}

void print_yesno(int x) {
printf("%s\n", x?"Yes":"No");
}

int main(void){ int a,b,c,d; read_input(&a,&b,&c,&d); int ok=can_full(a,b,c,d); print_yesno(ok); return 0;}
