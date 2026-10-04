#include <stdio.h>
#include <string.h>

void read_strings(char s[], char t[]) { scanf("%s%s", s, t); }

int try_extraction(char s[], char t[], int w, int c) { int s_len = strlen(s), t_len = strlen(t); char result[105]; int idx = 0; for(int i = c - 1; i < s_len; i += w) { result[idx++] = s[i]; } result[idx] = '\0'; return strcmp(result, t) == 0; }

int find_valid_pair(char s[], char t[]) { int s_len = strlen(s); for(int w = 1; w < s_len; w++) { for(int c = 1; c <= w; c++) { if(try_extraction(s, t, w, c)) return 1; } } return 0; }

int main() { char s[105], t[105]; read_strings(s, t); printf("%s\n", find_valid_pair(s, t) ? "Yes" : "No"); return 0; }
