#include <stdio.h>
#include <string.h>

void read_input(int *H,int *W,char s[][205]) {
scanf("%d%d", H,W); for(int i=0;i<*H;i++) scanf("%s", s[i]);
}

int can_rect(int H,int W,char s[][205]) {
int minr=H, maxr=-1, minc=W, maxc=-1;
for(int i=0;i<H;i++) for(int j=0;j<W;j++) if(s[i][j]=='#'){ if(i<minr) minr=i; if(i>maxr) maxr=i; if(j<minc) minc=j; if(j>maxc) maxc=j; }
if(maxr==-1) return 1;
for(int i=0;i<H;i++) for(int j=0;j<W;j++){
  if(i>=minr && i<=maxr && j>=minc && j<=maxc){ if(s[i][j]=='.') return 0; }
  else { if(s[i][j]=='#') return 0; }
}
return 1;
}

void print_yesno(int x) {
printf("%s\n", x?"Yes":"No");
}

int main(void){ int H,W; char s[205][205]; read_input(&H,&W,s); int ok=can_rect(H,W,s); print_yesno(ok); return 0;}
