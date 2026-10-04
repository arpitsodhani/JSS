#include <stdio.h>
#include <string.h>

void read_input(char *s1,char *s2) {
scanf("%s%s", s1,s2);
}

int is_consistent(int poison,const char *s1,const char *s2) {
int t_sick = (poison==1 || poison==2);
int a_sick = (poison==1 || poison==3);
int t_ok = (strcmp(s1,"sick")==0);
int a_ok = (strcmp(s2,"sick")==0);
return (t_sick==t_ok) && (a_sick==a_ok);
}

int find_poison(const char *s1,const char *s2) {
for(int p=1;p<=4;p++) if(is_consistent(p,s1,s2)) return p; return 1;
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ char s1[10],s2[10]; read_input(s1,s2); int ans=find_poison(s1,s2); print_int(ans); return 0; }
