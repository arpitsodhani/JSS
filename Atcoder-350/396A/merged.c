#include <stdio.h>

void read_input(int *n) {
scanf("%d", n);
}

int has_triple(int n) {
int prev=-1, run=0;
for(int i=0;i<n;i++){
  int x; scanf("%d", &x);
  if(x==prev) run++; else { prev=x; run=1; }
  if(run>=3) return 1;
}
return 0;
}

int main(void){ int n; read_input(&n); puts(has_triple(n)?"Yes":"No"); return 0; }
