#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int *M,long long *sx,long long *sy,char *S,long long *hx,long long *hy) {
scanf("%d%d%lld%lld", N,M,sx,sy);
scanf("%s", S);
for(int i=0;i<*N;i++) scanf("%lld%lld", &hx[i], &hy[i]);
}

void build_maps(int N,long long *hx,long long *hy) {
/* no-op placeholder: maps built in move */
}

int move_and_count(int M,long long *sx,long long *sy,char *S) {
/* build per-axis sorted lists with indices */
return 0;
}

void print_result(long long sx,long long sy,int cnt) {
/* handled in main */
}

int main(void) {
int N,M; long long sx,sy; static char S[200005];
static long long hx[200005], hy[200005];
read_input(&N,&M,&sx,&sy,S,hx,hy);
/* maps: for each x -> sorted y, and for each y -> sorted x */
typedef struct Node{ long long v; struct Node*next; } Node;
/* use sorted arrays per x and y via coordinate compression */
static long long xs[200005], ys[200005];
for(int i=0;i<N;i++){ xs[i]=hx[i]; ys[i]=hy[i]; }
int xn=N, yn=N;
for(int i=0;i<xn;i++) for(int j=i+1;j<xn;j++) if(xs[j]<xs[i]){ long long t=xs[i]; xs[i]=xs[j]; xs[j]=t; }
for(int i=0;i<yn;i++) for(int j=i+1;j<yn;j++) if(ys[j]<ys[i]){ long long t=ys[i]; ys[i]=ys[j]; ys[j]=t; }
int ux=0; for(int i=0;i<xn;i++) if(i==0||xs[i]!=xs[i-1]) xs[ux++]=xs[i];
int uy=0; for(int i=0;i<yn;i++) if(i==0||ys[i]!=ys[i-1]) ys[uy++]=ys[i];
/* adjacency lists by x and y (stored as sorted dynamic arrays) */
static int xcnt[200005], ycnt[200005];
for(int i=0;i<ux;i++) xcnt[i]=0; for(int i=0;i<uy;i++) ycnt[i]=0;
int *xid=(int*)malloc((size_t)N*sizeof(int));
int *yid=(int*)malloc((size_t)N*sizeof(int));
for(int i=0;i<N;i++){
  int lx=0,rx=ux-1; while(lx<=rx){ int md=(lx+rx)/2; if(xs[md]<hx[i]) lx=md+1; else rx=md-1; } xid[i]=lx;
  int ly=0,ry=uy-1; while(ly<=ry){ int md=(ly+ry)/2; if(ys[md]<hy[i]) ly=md+1; else ry=md-1; } yid[i]=ly;
  xcnt[xid[i]]++; ycnt[yid[i]]++;
}
long long **xlist=(long long**)malloc((size_t)ux*sizeof(long long*));
long long **ylist=(long long**)malloc((size_t)uy*sizeof(long long*));
for(int i=0;i<ux;i++){ xlist[i]=(long long*)malloc((size_t)xcnt[i]*sizeof(long long)); xcnt[i]=0; }
for(int i=0;i<uy;i++){ ylist[i]=(long long*)malloc((size_t)ycnt[i]*sizeof(long long)); ycnt[i]=0; }
for(int i=0;i<N;i++){ xlist[xid[i]][xcnt[xid[i]]++]=hy[i]; ylist[yid[i]][ycnt[yid[i]]++]=hx[i]; }
for(int i=0;i<ux;i++) for(int a=0;a<xcnt[i];a++) for(int b=a+1;b<xcnt[i];b++) if(xlist[i][b]<xlist[i][a]){ long long t=xlist[i][a]; xlist[i][a]=xlist[i][b]; xlist[i][b]=t; }
for(int i=0;i<uy;i++) for(int a=0;a<ycnt[i];a++) for(int b=a+1;b<ycnt[i];b++) if(ylist[i][b]<ylist[i][a]){ long long t=ylist[i][a]; ylist[i][a]=ylist[i][b]; ylist[i][b]=t; }
int visited=0;
for(int step=0; step<M; step++){
  char c=S[step]; long long nx=sx, ny=sy;
  if(c=='U') ny++; else if(c=='D') ny--; else if(c=='L') nx--; else if(c=='R') nx++;
  if(nx==sx){
    int idx=0, l=0,r=ux-1; while(l<=r){ int md=(l+r)/2; if(xs[md]<sx) l=md+1; else r=md-1; } idx=l; if(idx<ux && xs[idx]==sx){
      long long lo=sy<ny?sy:ny, hi=sy<ny?ny:sy;
      long long *arr=xlist[idx]; int sz=xcnt[idx];
      int a=0; while(a<sz && arr[a]<lo) a++; int b=a; while(b<sz && arr[b]<=hi) b++;
      if(b>a){ visited += (b-a);
        /* remove visited from both maps by marking with sentinel */
        for(int k=a;k<b;k++) arr[k]= (long long)4e18;
      }
    }
  } else {
    int idx=0, l=0,r=uy-1; while(l<=r){ int md=(l+r)/2; if(ys[md]<sy) l=md+1; else r=md-1; } idx=l; if(idx<uy && ys[idx]==sy){
      long long lo=sx<nx?sx:nx, hi=sx<nx?nx:sx;
      long long *arr=ylist[idx]; int sz=ycnt[idx];
      int a=0; while(a<sz && arr[a]<lo) a++; int b=a; while(b<sz && arr[b]<=hi) b++;
      if(b>a){ visited += (b-a); for(int k=a;k<b;k++) arr[k]=(long long)4e18; }
    }
  }
  sx=nx; sy=ny;
}
printf("%lld %lld %d\n", sx, sy, visited);
return 0;
}
