#include <stdio.h>
#include <string.h>

void read_input(int *n,char s[][55]) {
scanf("%d", n); for(int i=0;i<*n;i++) scanf("%s", s[i]);
}

void sort_by_len(int n,char s[][55]) {
for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) if(strlen(s[j])<strlen(s[i])){ char tmp[55]; strcpy(tmp,s[i]); strcpy(s[i],s[j]); strcpy(s[j],tmp); }
}

void concat(int n,char s[][55],char *out) {
out[0]='\0'; for(int i=0;i<n;i++) strcat(out,s[i]);
}

void print_str(const char *s) {
printf("%s\n", s);
}

int main(void){ int n; char s[55][55]; char out[3000]; read_input(&n,s); sort_by_len(n,s); concat(n,s,out); print_str(out); return 0; }
