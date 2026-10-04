#include <stdio.h>

int read_n(void) {
int n; scanf("%d", &n); return n;
}

int is_strict(int n) {
int prev; scanf("%d", &prev);
for(int i=1;i<n;i++){
  int x; scanf("%d", &x);
  if(!(prev<x)) return 0;
  prev=x;
}
return 1;
}

int main(void){ int n=read_n(); puts(is_strict(n)?"Yes":"No"); return 0; }
