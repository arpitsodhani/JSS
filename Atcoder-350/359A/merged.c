#include <stdio.h>
#include <string.h>

int read_count() { int n; scanf("%d", &n); return n; }

int count_takahashi(int n) { int count = 0; for(int i = 0; i < n; i++) { char s[20]; scanf("%s", s); if(strcmp(s, "Takahashi") == 0) count++; } return count; }

int main() { int n = read_count(); printf("%d\n", count_takahashi(n)); return 0; }
