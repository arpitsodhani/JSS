#include <stdio.h>
#include <stdlib.h>

void read_input(int *H,int *W,int *K,char **S){ scanf("%d%d%d", H,W,K); *S=(char*)malloc((size_t)(*H)*(*W+1)); for(int i=0;i<*H;i++) scanf("%s", (*S)+i*(*W+1)); }

long long dfs(int r,int c,int H,int W,int K,char *S,char *vis){
    if(K==0) return 1;
    long long ans=0;
    int dr[4]={-1,1,0,0}, dc[4]={0,0,-1,1};
    for(int k=0;k<4;k++){
        int nr=r+dr[k], nc=c+dc[k];
        if(nr<0||nr>=H||nc<0||nc>=W) continue;
        if(S[nr*(W+1)+nc]=='#') continue;
        if(vis[nr*W+nc]) continue;
        vis[nr*W+nc]=1;
        ans += dfs(nr,nc,H,W,K-1,S,vis);
        vis[nr*W+nc]=0;
    }
    return ans;
}

long long count_paths(int H,int W,int K,char *S){ long long ans=0; char *vis=(char*)calloc((size_t)H*W,1); for(int i=0;i<H;i++) for(int j=0;j<W;j++) if(S[i*(W+1)+j]=='.'){ vis[i*W+j]=1; ans+=dfs(i,j,H,W,K,S,vis); vis[i*W+j]=0; } free(vis); return ans; }

void print_answer(long long ans){ printf("%lld\n", ans); }

int main(void){ int H,W,K; char *S=NULL; read_input(&H,&W,&K,&S); long long ans=count_paths(H,W,K,S); print_answer(ans); free(S); return 0; }
