#include <stdio.h>
#include <string.h>

int read_input(char *s) {
scanf("%s", s); return (int)strlen(s);
}

void filter_twos(const char *s,char *out) {
int k=0; for(int i=0;s[i];i++) if(s[i]=='2') out[k++]=s[i]; out[k]='\0';
}

void print_str(const char *s) {
printf("%s\n", s);
}

int main(void){ char s[205],out[205]; read_input(s); filter_twos(s,out); print_str(out); return 0; }
