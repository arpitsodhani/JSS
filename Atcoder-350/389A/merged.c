#include <stdio.h>

void read_input(char *s) {
scanf("%s", s);
}

int product(const char *s) {
return (s[0]-'0')*(s[2]-'0');
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ char s[10]; read_input(s); int ans=product(s); print_int(ans); return 0;}
