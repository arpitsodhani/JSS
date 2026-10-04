#include <stdio.h>
#include <string.h>

int read_input(char *s) {
scanf("%s", s); return (int)strlen(s);
}

long long count_abc(const char *s,int n) {
long long ans=0;
for(int j=0;j<n;j++) if(s[j]=='B'){
  for(int d=1;j-d>=0 && j+d<n;d++) if(s[j-d]=='A' && s[j+d]=='C') ans++;
}
return ans;
}

void print_ll(long long x) {
printf("%lld\n", x);
}

int main(void){ char s[205]; int n=read_input(s); long long ans=count_abc(s,n); print_ll(ans); return 0; }
