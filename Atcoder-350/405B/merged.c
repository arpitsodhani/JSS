#include <stdio.h>
#include <string.h>

void read_s(char *s) {
scanf("%200s", s);
}

int count_sub(const char *s) {
int n=(int)strlen(s), ans=0; for(int i=0;i+7<=n;i++) if(strncmp(s+i,"ATCODER",7)==0) ans++; return ans;
}

void print_ans(int x) {
printf("%d\n", x);
}

int main(void){ char s[205]; read_s(s); int ans=count_sub(s); print_ans(ans); return 0; }
