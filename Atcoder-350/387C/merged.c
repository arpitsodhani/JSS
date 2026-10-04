#include <stdio.h>
#include <string.h>

int read_input(char *s) {
scanf("%s", s); return (int)strlen(s);
}

int count_x(const char *s,int n) {
int c=0; for(int i=0;i<n;i++) if(s[i]=='x') c++; return c;
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ char s[400005]; int n=read_input(s); int ans=count_x(s,n); print_int(ans); return 0;}
