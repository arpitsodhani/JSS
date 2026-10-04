#include <stdio.h>
#include <string.h>

int read_s(char *s) {
scanf("%100s", s); return (int)strlen(s);
}

int min_insertions(const char *s, int n) {
int ins=0;
char expect='i';
for(int i=0;i<n;i++){
  char ch=s[i];
  while(ch!=expect){
    ins++;
    expect = (expect=='i')?'o':'i';
  }
  expect = (expect=='i')?'o':'i';
}
if(expect=='o') ins++;
return ins;
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ static char s[105]; int n=read_s(s); int ans=min_insertions(s,n); print_int(ans); return 0; }
