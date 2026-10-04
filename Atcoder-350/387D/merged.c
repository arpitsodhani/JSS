#include <stdio.h>
#include <string.h>

void read_input(int *H,int *W,char s[][505]) {
scanf("%d%d", H,W); for(int i=0;i<*H;i++) scanf("%s", s[i]);
}

int solve(int H,int W,char s[][505]) {
int ans=0; for(int i=0;i<H;i++) for(int j=0;j<W;j++) if(s[i][j]=='#') ans++; return ans;
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ int H,W; char s[505][505]; read_input(&H,&W,s); int ans=solve(H,W,s); print_int(ans); return 0;}
