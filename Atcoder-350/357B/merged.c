#include <stdio.h>
#include <string.h>
#include <ctype.h>

void convert_case(char s[]) { int upper = 0, lower = 0; for(int i = 0; s[i]; i++) { if(isupper(s[i])) upper++; else lower++; } if(upper > lower) { for(int i = 0; s[i]; i++) s[i] = toupper(s[i]); } else { for(int i = 0; s[i]; i++) s[i] = tolower(s[i]); } }

int main() { char s[105]; read_input(s); convert_case(s); printf("%s\n", s); return 0; }

void read_input(char s[]) { scanf("%s", s); }

