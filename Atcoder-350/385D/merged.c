#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int *M,long long *sx,long long *sy,char *D,long long *C,long long *X,long long *Y){
    scanf("%d%d%lld%lld", N,M,sx,sy);
    for(int i=0;i<*N;i++) scanf("%lld%lld", &X[i], &Y[i]);
    for(int i=0;i<*M;i++) scanf(" %c%lld", &D[i], &C[i]);
}

int count_houses(int N,int M,long long sx,long long sy,char *D,long long *C,long long *X,long long *Y,long long *fx,long long *fy){
    char *vis = (char*)calloc((size_t)N,1);
    int visited=0;
    for(int i=0;i<M;i++){
        long long nx=sx, ny=sy;
        if(D[i]=='U') ny+=C[i];
        else if(D[i]=='D') ny-=C[i];
        else if(D[i]=='L') nx-=C[i];
        else if(D[i]=='R') nx+=C[i];
        long long x1=sx, y1=sy, x2=nx, y2=ny;
        for(int h=0; h<N; h++){
            if(vis[h]) continue;
            long long hx=X[h], hy=Y[h];
            if(x1==x2 && hx==x1){
                long long lo = y1<y2?y1:y2;
                long long hi = y1<y2?y2:y1;
                if(hy>=lo && hy<=hi){ vis[h]=1; visited++; }
            } else if(y1==y2 && hy==y1){
                long long lo = x1<x2?x1:x2;
                long long hi = x1<x2?x2:x1;
                if(hx>=lo && hx<=hi){ vis[h]=1; visited++; }
            }
        }
        sx=nx; sy=ny;
    }
    free(vis);
    *fx=sx; *fy=sy;
    return visited;
}

void print_answer(long long x,long long y,int cnt){ printf("%lld %lld %d\n", x,y,cnt); }

int main(void){
    int N,M;
    long long sx,sy;
    char *D = (char*)malloc(300000);
    long long *C = (long long*)malloc((size_t)300000*sizeof(long long));
    long long *X = (long long*)malloc((size_t)300000*sizeof(long long));
    long long *Y = (long long*)malloc((size_t)300000*sizeof(long long));
    read_input(&N,&M,&sx,&sy,D,C,X,Y);
    long long fx,fy;
    int cnt = count_houses(N,M,sx,sy,D,C,X,Y,&fx,&fy);
    print_answer(fx,fy,cnt);
    free(D); free(C); free(X); free(Y);
    return 0;
}
