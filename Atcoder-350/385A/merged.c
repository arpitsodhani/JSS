#include <stdio.h>

void read_input(int *a,int *b,int *c){
    scanf("%d%d%d", a,b,c);
}

int can_split(int a,int b,int c){
    int sum = a+b+c;
    if(a==b && b==c) return 1;
    if(sum%2) return 0;
    int half = sum/2;
    return (a==half || b==half || c==half);
}

void print_answer(int ok){
    printf("%s\n", ok? "Yes":"No");
}

int main(void){
    int a,b,c;
    read_input(&a,&b,&c);
    int ok = can_split(a,b,c);
    print_answer(ok);
    return 0;
}
