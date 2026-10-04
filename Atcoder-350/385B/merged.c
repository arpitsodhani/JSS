#include <stdio.h>
#include <stdlib.h>

void read_input(int *H,int *W,int *x,int *y,char *T,char **grid){
    scanf("%d%d%d%d", H,W,x,y);
    scanf("%s", T);
    *grid = (char*)malloc((size_t)(*H)*(*W+1));
    for(int i=0;i<*H;i++){
        scanf("%s", (*grid)+i*(*W+1));
    }
}

int simulate(int H,int W,int x,int y,char *T,char *grid,int *fx,int *fy){
    int visited = 0;
    char *mark = (char*)calloc((size_t)H*W,1);
    int len = 0; while(T[len]) len++;
    int r = x-1, c = y-1;
    if(grid[r*(W+1)+c]=='@' && !mark[r*W+c]){ mark[r*W+c]=1; visited++; }
    for(int i=0;i<len;i++){
        int nr=r, nc=c;
        if(T[i]=='U') nr--;
        else if(T[i]=='D') nr++;
        else if(T[i]=='L') nc--;
        else if(T[i]=='R') nc++;
        if(nr>=0 && nr<H && nc>=0 && nc<W && grid[nr*(W+1)+nc]!='#'){ r=nr; c=nc; }
        if(grid[r*(W+1)+c]=='@' && !mark[r*W+c]){ mark[r*W+c]=1; visited++; }
    }
    free(mark);
    *fx=r+1; *fy=c+1;
    return visited;
}

void print_answer(int fx,int fy,int cnt){
    printf("%d %d %d\n", fx, fy, cnt);
}

int main(void){
    int H,W,x,y;
    char T[200005];
    char *grid=NULL;
    read_input(&H,&W,&x,&y,T,&grid);
    int fx,fy;
    int cnt = simulate(H,W,x,y,T,grid,&fx,&fy);
    print_answer(fx,fy,cnt);
    free(grid);
    return 0;
}
