#include <stdio.h>
#include <stdlib.h>

void read_input(int *H,int *W,int *D,char **S){ scanf("%d%d%d", H,W,D); *S=(char*)malloc((size_t)(*H)*(*W+1)); for(int i=0;i<*H;i++) scanf("%s", (*S)+i*(*W+1)); }

int count_humidified(int H,int W,int D,char *S){
    int n=H*W;
    int *dist=(int*)malloc((size_t)n*sizeof(int));
    for(int i=0;i<n;i++) dist[i]=-1;
    int *qr=(int*)malloc((size_t)n*sizeof(int));
    int *qc=(int*)malloc((size_t)n*sizeof(int));
    int head=0, tail=0;
    for(int i=0;i<H;i++) for(int j=0;j<W;j++){
        if(S[i*(W+1)+j]=='H'){
            dist[i*W+j]=0;
            qr[tail]=i; qc[tail]=j; tail++;
        }
    }
    int dr[4]={-1,1,0,0}, dc[4]={0,0,-1,1};
    while(head<tail){
        int r=qr[head], c=qc[head]; head++;
        for(int k=0;k<4;k++){
            int nr=r+dr[k], nc=c+dc[k];
            if(nr<0||nr>=H||nc<0||nc>=W) continue;
            if(S[nr*(W+1)+nc]=='#') continue;
            int id=nr*W+nc;
            if(dist[id]==-1){
                dist[id]=dist[r*W+c]+1;
                if(dist[id]<=D){ qr[tail]=nr; qc[tail]=nc; tail++; }
            }
        }
    }
    int cnt=0;
    for(int i=0;i<H;i++) for(int j=0;j<W;j++){
        if(S[i*(W+1)+j]!='#' && dist[i*W+j]!=-1 && dist[i*W+j]<=D) cnt++;
    }
    free(dist); free(qr); free(qc);
    return cnt;
}

void print_answer(int ans){ printf("%d\n", ans); }

int main(void){ int H,W,D; char *S=NULL; read_input(&H,&W,&D,&S); int ans=count_humidified(H,W,D,S); print_answer(ans); free(S); return 0; }
