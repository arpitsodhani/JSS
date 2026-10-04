#include <stdio.h>
#include <stdlib.h>

int read_input(char *s) {
scanf("%s", s); int n=0; while(s[n]) n++; return n;
}

long long min_swaps(const char *s,int n) {
int pos[200005]; int cnt=0;
for(int i=0;i<n;i++) if(s[i]=='1') pos[cnt++]=i;
int mid=cnt/2;
long long ans=0;
for(int i=0;i<cnt;i++) ans+= llabs((long long)pos[i] - (long long)(pos[mid]-mid+i));
return ans;
}

void print_ll(long long x) {
printf("%lld\n", x);
}

int main(void){ static char s[200005]; int n=read_input(s); long long ans=min_swaps(s,n); print_ll(ans); return 0; }
