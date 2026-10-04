#include <stdio.h>
#include <string.h>

void read_s(char *s) {
scanf("%200s", s);
}

int is_palindrome(const char *s) {
int n=(int)strlen(s); int l=0,r=n-1; while(l<r){ if(s[l]!=s[r]) return 0; l++; r--; } return 1;
}

void print_ans(int ok) {
puts(ok?"Yes":"No");
}

int main(void){ char s[205]; read_s(s); int ok=is_palindrome(s); print_ans(ok); return 0; }
