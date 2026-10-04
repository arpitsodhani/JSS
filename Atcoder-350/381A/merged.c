#include <stdio.h>
#include <string.h>

void read_input(char *S){ scanf("%s", S); }

int is_1122(char *S){
    int n=strlen(S);
    int mid=n/2;
    if(n%2==0) return 0;
    if(S[mid]!='/') return 0;
    for(int i=0;i<mid;i++) if(S[i]!='1') return 0;
    for(int i=mid+1;i<n;i++) if(S[i]!='2') return 0;
    return 1;
}

void print_answer(int ok){ printf("%s\n", ok?"Yes":"No"); }

int main(void){ char S[205]; read_input(S); int ok=is_1122(S); print_answer(ok); return 0; }
