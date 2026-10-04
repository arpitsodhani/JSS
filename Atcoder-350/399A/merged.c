#include <stdio.h>
#include <string.h>

void read_strings(char *s, char *t) {
scanf("%1000s %1000s", s, t);
}

int can_match(const char *s, const char *t) {
int n=(int)strlen(s);
if((int)strlen(t)!=n) return 0;
for(int i=0;i<n;i++) if(s[i]!=t[i]) return 0;
return 1;
}

int main(void){ char s[1100],t[1100]; read_strings(s,t); puts(can_match(s,t)?"Yes":"No"); return 0; }
