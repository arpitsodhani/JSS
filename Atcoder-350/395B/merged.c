#include <stdio.h>

int read_n(void) {
int n; scanf("%d", &n); return n;
}

void fill_grid(int n, char *g) {
for(int i=0;i<n*n;i++) g[i]='?';
for(int layer=1;layer<=n;layer++){
  int j=n+1-layer;
  if(layer>j) continue;
  char ch = (layer%2==1)?'#':'.';
  for(int r=layer-1;r<=j-1;r++) for(int c=layer-1;c<=j-1;c++) g[r*n+c]=ch;
}
}

void print_grid(int n, const char *g) {
for(int r=0;r<n;r++){
  for(int c=0;c<n;c++) putchar(g[r*n+c]);
  putchar('\n');
}
}

int main(void){ int n=read_n(); char *g=(char*)malloc((size_t)n*(size_t)n); fill_grid(n,g); print_grid(n,g); free(g); return 0; }
