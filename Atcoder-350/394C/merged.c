#include <stdio.h>
#include <string.h>

void read_input(char *s) {
scanf("%s", s);
}

void transform(char *s) {
int n=(int)strlen(s);
char *stk=(char*)malloc((size_t)n+5); int top=0;
for(int i=0;i<n;i++){
  stk[top++]=s[i];
  if(top>=2 && stk[top-2]=='W' && stk[top-1]=='A'){ stk[top-2]='A'; stk[top-1]='C'; }
}
for(int i=0;i<top;i++) s[i]=stk[i]; s[top]='\0';
free(stk);
}

void print_str(const char *s) {
printf("%s\n", s);
}

int main(void){ char s[400005]; read_input(s); transform(s); print_str(s); return 0; }
