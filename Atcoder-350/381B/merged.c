#include <stdio.h>
#include <string.h>

void read_input(char *S){ scanf("%s", S); }

int check_pairs(char *S){
    int n=strlen(S);
    if(n%2) return 0;
    int cnt[26]={0};
    for(int i=0;i<n;i++) cnt[S[i]-'a']++;
    for(int c=0;c<26;c++) if(cnt[c]!=0 && cnt[c]!=2) return 0;
    for(int i=0;i<n;i+=2) if(S[i]!=S[i+1]) return 0;
    return 1;
}

void print_answer(int ok){ printf("%s\n", ok?"Yes":"No"); }

int main(void){ char S[205]; read_input(S); int ok=check_pairs(S); print_answer(ok); return 0; }
