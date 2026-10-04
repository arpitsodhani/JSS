#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_input(int *h, int *w, int *a, int *b, int *c, int *d, char *grid) {
scanf("%d %d", h, w);
for(int i=0;i<*h;i++){
  scanf("%s", &grid[i*(*w)]);
}
scanf("%d %d %d %d", a, b, c, d);
*a -= 1; *b -= 1; *c -= 1; *d -= 1;
}

int min_kicks(int h, int w, int a, int b, int c, int d, const char *grid) {
int n=h*w;
int *dist=(int*)malloc((size_t)n*sizeof(int));
for(int i=0;i<n;i++) dist[i]=n+5;
int *dq=(int*)malloc((size_t)(n*2+5)*sizeof(int));
int head=n, tail=n;
int s=a*w+b, t=c*w+d;
dist[s]=0; dq[head]=s;
const int dx[4]={-1,1,0,0};
const int dy[4]={0,0,-1,1};
while(head<=tail){
  int v=dq[head++];
  if(v==t) break;
  int x=v/w, y=v%w;
  for(int dir=0;dir<4;dir++){
    int wall=0;
    for(int step=1;step<=2;step++){
      int nx=x+dx[dir]*step;
      int ny=y+dy[dir]*step;
      if(nx<0||nx>=h||ny<0||ny>=w) break;
      char ch=grid[nx*w+ny];
      if(ch=='#') wall=1;
      int to=nx*w+ny;
      if(!wall){
        if(step==1){
          if(ch=='.' && dist[to]>dist[v]){ dist[to]=dist[v]; dq[--head]=to; }
        }
      } else {
        if(dist[to]>dist[v]+1){ dist[to]=dist[v]+1; dq[++tail]=to; }
      }
    }
  }
}
int ans=dist[t];
free(dist); free(dq);
return ans;
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ int h,w,a,b,c,d; static char grid[2005*2005]; read_input(&h,&w,&a,&b,&c,&d,grid); int ans=min_kicks(h,w,a,b,c,d,grid); print_int(ans); return 0; }
