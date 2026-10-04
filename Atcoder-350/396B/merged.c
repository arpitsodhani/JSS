#include <stdio.h>

int read_q(void) {
int q; scanf("%d", &q); return q;
}

void process(int q) {
int st[500]; int top=0;
for(int i=0;i<100;i++) st[top++]=0;
for(int qi=0;qi<q;qi++){
  int t; scanf("%d", &t);
  if(t==1){ int x; scanf("%d", &x); st[top++]=x; }
  else { int x=st[--top]; printf("%d\n", x); }
}
}

int main(void){ int q=read_q(); process(q); return 0; }
