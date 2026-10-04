#include <stdio.h>
#include <string.h>

int read_n(void) {
int n; scanf("%d", &n); return n;
}

void build_string(int n, char *out) {
for(int i=0;i<n;i++) out[i]='-'; out[n]='\0'; if(n%2==1){ out[n/2]='='; } else { out[n/2-1]='='; out[n/2]='='; }
}

void print_s(const char *s) {
puts(s);
}

int main(void){ int n=read_n(); static char s[205]; build_string(n,s); print_s(s); return 0; }
