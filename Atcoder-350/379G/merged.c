#include <stdio.h>
#include <stdlib.h>

void read_input(int *H,int *W,char **S){ scanf("%d%d", H,W); *S=(char*)malloc((size_t)(*H)*(*W+1)); for(int i=0;i<*H;i++) scanf("%s", (*S)+i*(*W+1)); }

int idx(int r,int c,int W){ return r*W+c; }

int cell_value(char ch){ if(ch=='?') return 0; return ch-'0'; }

int check_fixed(char ch,int val){ int f=cell_value(ch); return (f==0 || f==val); }

int can_place(int r,int c,int W,char *S,int *assign,int val){ char ch=S[idx(r,c,W)]; if(!check_fixed(ch,val)) return 0; if(r>0 && assign[idx(r-1,c,W)]==val) return 0; if(c>0 && assign[idx(r,c-1,W)]==val) return 0; return 1; }

long long dfs_count(int pos,int H,int W,char *S,int *assign){
    const long long MOD=998244353;
    if(pos==H*W) return 1;
    int r=pos/W, c=pos%W;
    long long ans=0;
    for(int val=1; val<=3; val++){
        if(can_place(r,c,W,S,assign,val)){
            assign[pos]=val;
            ans=(ans+dfs_count(pos+1,H,W,S,assign))%MOD;
            assign[pos]=0;
        }
    }
    return ans;
}

int small_enough(int H,int W){ return H*W<=12; }

long long count_colorings(int H,int W,char *S){
    if(!small_enough(H,W)) return 0;
    int *assign=(int*)calloc((size_t)H*W,sizeof(int));
    long long ans=dfs_count(0,H,W,S,assign);
    free(assign);
    return ans;
}

void print_answer(long long ans){ printf("%lld\n", ans); }

int main(void){ int H,W; char *S=NULL; read_input(&H,&W,&S); long long ans=count_colorings(H,W,S); print_answer(ans); free(S); return 0; }
