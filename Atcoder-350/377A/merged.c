#include <stdio.h>
#include <string.h>

void read_input(char *S){ scanf("%s", S); }

int check_perm(char *S){ int seen[26]={0}; for(int i=0;i<3;i++) seen[S[i]-'A']++; return (seen['A'-'A']&&seen['B'-'A']&&seen['C'-'A']); }

void print_answer(int ok){ printf("%s\n", ok?"Yes":"No"); }

int main(void){ char S[10]; read_input(S); int ok=check_perm(S); print_answer(ok); return 0; }
