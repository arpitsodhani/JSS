#include <stdio.h>
#include <string.h>

void read_input(char *s) {
scanf("%s", s);
}

void reverse(char *s) {
int n=strlen(s); for(int i=0;i<n/2;i++){ char t=s[i]; s[i]=s[n-1-i]; s[n-1-i]=t; }
}

void print_str(const char *s) {
printf("%s\n", s);
}

int main(void){ char s[400005]; read_input(s); reverse(s); print_str(s); return 0;}
