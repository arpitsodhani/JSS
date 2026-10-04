#include <stdio.h>
#include <string.h>

void read_s(char *s) {
scanf("%5000s", s);
}

int longest_pal(const char *s) {
int n=(int)strlen(s); int best=1;
for(int c=0;c<n;c++){
  int l=c,r=c;
  while(l>=0 && r<n && s[l]==s[r]){ int len=r-l+1; if(len>best) best=len; l--; r++; }
  l=c; r=c+1;
  while(l>=0 && r<n && s[l]==s[r]){ int len=r-l+1; if(len>best) best=len; l--; r++; }
}
return best;
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ static char s[6005]; read_s(s); int ans=longest_pal(s); print_int(ans); return 0; }
