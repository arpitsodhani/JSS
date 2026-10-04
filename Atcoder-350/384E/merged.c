#include <stdio.h>
#include <stdlib.h>

void read_input(int *H,int *W,long long *X,int *P,int *Q,long long **S){
    scanf("%d%d%lld", H,W,X);
    scanf("%d%d", P,Q);
    *S=(long long*)malloc((size_t)(*H)*(*W)*sizeof(long long));
    for(int i=0;i<*H;i++) for(int j=0;j<*W;j++) scanf("%lld", &(*S)[i*(*W)+j]);
}

long long max_strength(int H,int W,long long X,int P,int Q,long long *S){
    int n=H*W;
    char *vis=(char*)calloc((size_t)n,1);
    int *qh=(int*)malloc((size_t)n*sizeof(int));
    int *qw=(int*)malloc((size_t)n*sizeof(int));
    int head=0,tail=0;
    int start=(P-1)*W+(Q-1);
    vis[start]=1;
    long long cur = S[start];
    int dr[4]={-1,1,0,0};
    int dc[4]={0,0,-1,1};
    // min-heap using arrays (simple selection each time)
    long long *candVal=(long long*)malloc((size_t)n*sizeof(long long));
    int *candPos=(int*)malloc((size_t)n*sizeof(int));
    int candN=0;
    qh[tail]=P-1; qw[tail]=Q-1; tail++;
    while(head<tail){
        int r=qh[head], c=qw[head]; head++;
        for(int k=0;k<4;k++){
            int nr=r+dr[k], nc=c+dc[k];
            if(nr<0||nr>=H||nc<0||nc>=W) continue;
            int id=nr*W+nc;
            if(vis[id]) continue;
            vis[id]=2; // seen
            candVal[candN]=S[id];
            candPos[candN]=id;
            candN++;
        }
        // try to absorb as much as possible
        int changed=1;
        while(changed){
            changed=0;
            // find smallest candidate
            long long best=0; int bestIdx=-1;
            for(int i=0;i<candN;i++){
                if(candVal[i]<0) continue;
                if(bestIdx==-1 || candVal[i]<best){ best=candVal[i]; bestIdx=i; }
            }
            if(bestIdx!=-1 && best*X < cur){
                cur += best;
                int id=candPos[bestIdx];
                candVal[bestIdx]=-1;
                int rr=id/W, cc=id%W;
                qh[tail]=rr; qw[tail]=cc; tail++;
                changed=1;
            }
        }
    }
    free(candVal); free(candPos); free(qh); free(qw); free(vis);
    return cur;
}

void print_answer(long long s){ printf("%lld\n", s); }

int main(void){
    int H,W,P,Q; long long X; long long *S=NULL;
    read_input(&H,&W,&X,&P,&Q,&S);
    long long ans = max_strength(H,W,X,P,Q,S);
    print_answer(ans);
    free(S);
    return 0;
}
