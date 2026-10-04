#include <stdio.h>
#include <string.h>

void read_input(char *s,char *t) {
scanf("%s%s", s,t);
}

int can_edit(const char *s,const char *t) {
int n=strlen(s), m=strlen(t);
if(n==m){ int diff=0; for(int i=0;i<n;i++) if(s[i]!=t[i]) diff++; return diff<=1; }
if(n+1==m){ int i=0,j=0,used=0; while(i<n && j<m){ if(s[i]==t[j]){i++;j++;} else { if(used) return 0; used=1; j++; } } return 1; }
if(m+1==n){ int i=0,j=0,used=0; while(i<n && j<m){ if(s[i]==t[j]){i++;j++;} else { if(used) return 0; used=1; i++; } } return 1; }
return 0;
}

void print_yesno(int x) {
printf("%s\n", x?"Yes":"No");
}

int main(void){ char s[600000],t[600000]; read_input(s,t); int ok=can_edit(s,t); print_yesno(ok); return 0;}
