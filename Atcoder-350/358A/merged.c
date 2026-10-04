#include <stdio.h>
#include <string.h>

void read_strings(char s[], char t[]) { scanf("%s%s", s, t); }

int check_match(char s[], char t[]) { return (strcmp(s, "AtCoder") == 0 && strcmp(t, "Land") == 0); }

int main() { char s[105], t[105]; read_strings(s, t); printf("%s\n", check_match(s, t) ? "Yes" : "No"); return 0; }
