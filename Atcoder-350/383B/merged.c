#include <stdio.h>
#include <stdlib.h>

void read_input(int *H,int *W,int *D,char *S){ scanf("%d%d%d", H,W,D); for(int i=0;i<*H;i++) scanf("%s", S+i*(*W+1)); }

int max_humidified(int H,int W,int D,char *S){
    int cells[105][2]; int n=0;
    for(int i=0;i<H;i++) for(int j=0;j<W;j++) if(S[i*(W+1)+j]=='.'){ cells[n][0]=i; cells[n][1]=j; n++; }
    int best=0;
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            int cnt=0;
            for(int r=0;r<n;r++){
                int d1 = abs(cells[r][0]-cells[i][0]) + abs(cells[r][1]-cells[i][1]);
                int d2 = abs(cells[r][0]-cells[j][0]) + abs(cells[r][1]-cells[j][1]);
                if(d1<=D || d2<=D) cnt++;
            }
            if(cnt>best) best=cnt;
        }
    }
    return best;
}

void print_answer(int ans){ printf("%d\n", ans); }

int main(void){ int H,W,D; static char S[1200]; read_input(&H,&W,&D,S); int ans=max_humidified(H,W,D,S); print_answer(ans); return 0; }
