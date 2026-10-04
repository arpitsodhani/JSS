#include <stdio.h>
#include <string.h>

int read_input(char *s) {
scanf("%s", s); return (int)strlen(s);
}

int min_presses(const char *s,int n) {
int dp[205]; for(int i=0;i<=n;i++) dp[i]=1e9; dp[0]=0;
const char *btns[] = {"00","0","1","2","3","4","5","6","7","8","9"};
int blen[] = {2,1,1,1,1,1,1,1,1,1,1};
for(int i=0;i<n;i++) if(dp[i]<1e9){
  for(int b=0;b<11;b++){
    int L=blen[b]; if(i+L>n) continue; int ok=1; for(int k=0;k<L;k++) if(s[i+k]!=btns[b][k]) ok=0; if(ok && dp[i]+1<dp[i+L]) dp[i+L]=dp[i]+1;
  }
}
return dp[n];
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ char s[205]; int n=read_input(s); int ans=min_presses(s,n); print_int(ans); return 0;}
