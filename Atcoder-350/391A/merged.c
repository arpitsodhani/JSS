#include <stdio.h>
#include <string.h>

void read_input(char *s) {
scanf("%s", s);
}

void opposite(const char *s,char *out) {
if(strcmp(s,"N")==0) strcpy(out,"S");
else if(strcmp(s,"S")==0) strcpy(out,"N");
else if(strcmp(s,"E")==0) strcpy(out,"W");
else if(strcmp(s,"W")==0) strcpy(out,"E");
else if(strcmp(s,"NE")==0) strcpy(out,"SW");
else if(strcmp(s,"NW")==0) strcpy(out,"SE");
else if(strcmp(s,"SE")==0) strcpy(out,"NW");
else strcpy(out,"NE");
}

void print_str(const char *s) {
printf("%s\n", s);
}

int main(void){ char s[10],out[10]; read_input(s); opposite(s,out); print_str(out); return 0;}
