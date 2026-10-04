#include <stdio.h>
#include <string.h>

void read_arrangement(char s[]) { scanf("%s", s); }

int check_rice_before_miso(char s[]) { int r_pos = -1, m_pos = -1; for(int i = 0; i < 3; i++) { if(s[i] == 'R') r_pos = i; if(s[i] == 'M') m_pos = i; } return r_pos < m_pos; }

int main() { char s[5]; read_arrangement(s); printf("%s\n", check_rice_before_miso(s) ? "Yes" : "No"); return 0; }
