#include <stdio.h>

void read_input(int *N){ scanf("%d", N); }

int check_digits(int N){
    int cnt1=0,cnt2=0,cnt3=0;
    for(int i=0;i<6;i++){
        int d=N%10; N/=10;
        if(d==1) cnt1++;
        if(d==2) cnt2++;
        if(d==3) cnt3++;
    }
    return (cnt1==1 && cnt2==2 && cnt3==3);
}

void print_answer(int ok){ printf("%s\n", ok?"Yes":"No"); }

int main(void){ int N; read_input(&N); int ok=check_digits(N); print_answer(ok); return 0; }
