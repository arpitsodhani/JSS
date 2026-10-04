#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, int *r, int *c, char *s) {
scanf("%d %d %d", n, r, c); scanf("%s", s);
}

void apply_move(char mv, int *dx, int *dy) {
if(mv=='N') (*dx)--;
else if(mv=='S') (*dx)++;
else if(mv=='W') (*dy)--;
else (*dy)++;
}

unsigned long long pack(int x, int y) {
return ((unsigned long long)(unsigned int)(x+1000000) << 32) ^ (unsigned int)(y+1000000);
}

void simulate(int n, int r, int c, const char *s) {
int dx=0, dy=0;
int cap=n+5; unsigned long long *set=(unsigned long long*)malloc((size_t)cap*sizeof(unsigned long long)); int sz=0;
set[sz++]=pack(0,0);
for(int t=1;t<=n;t++){
  apply_move(s[t-1], &dx, &dy);
  int ox=-dx, oy=-dy;
  unsigned long long key0=pack(ox,oy);
  int has0=0;
  for(int i=0;i<sz;i++) if(set[i]==key0){ has0=1; break; }
  if(!has0){ if(sz==cap){ cap*=2; set=(unsigned long long*)realloc(set,(size_t)cap*sizeof(unsigned long long)); }
    set[sz++]=key0;
  }
  unsigned long long q=pack(r-dx,c-dy);
  int has=0;
  for(int i=0;i<sz;i++) if(set[i]==q){ has=1; break; }
  putchar(has?'1':'0');
}
putchar('\n');
free(set);
}

int main(void){ int n,r,c; static char s[300005]; read_input(&n,&r,&c,s); simulate(n,r,c,s); return 0; }
