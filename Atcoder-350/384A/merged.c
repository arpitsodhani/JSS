#include <stdio.h>
#include <string.h>

void read_input(char *S,char *c1,char *c2){
    scanf("%s", S);
    scanf(" %c %c", c1, c2);
}

void replace_chars(char *S,char c1,char c2){
    for(int i=0; S[i]; i++){
        if(S[i]!=c1) S[i]=c2;
    }
}

void print_answer(char *S){ printf("%s\n", S); }

int main(void){ char S[205]; char c1,c2; read_input(S,&c1,&c2); replace_chars(S,c1,c2); print_answer(S); return 0; }
