#include <stdio.h>

void factorize(int n) {
    int first = 1;
    for (int i = 2; i <= n; i++) {
        while (n % i == 0) {
            if (!first) printf(" ");
            printf("%d", i);
            first = 0;
            n /= i;
        }
    }
    printf("\n");
}

int main(void) {
    int n;
    scanf("%d", &n);
    factorize(n);
    return 0;
}

void get_factors(int num) {
    int found = 0;
    for (int i = 2; i <= num; i++) {
        while (num % i == 0) {
            if (found > 0) printf(" ");
            printf("%d", i);
            found++;
            num /= i;
        }
    }
    printf("\n");
}

void prime_factors(int n) {
    int first=1;
    for (int i=2;i<=n;i++) while(n%i==0){if(!first)printf(" ");printf("%d",i);first=0;n/=i;}
    printf("\n");
}

void factor_list(int num) {
    int cnt=0;
    for (int d=2;d<=num;d++) while(num%d==0){if(cnt>0)printf(" ");printf("%d",d);cnt++;num/=d;}
    printf("\n");
}

void decompose(int v) {
    int printed=0;
    int f=2;
    while(f<=v){while(v%f==0){if(printed)printf(" ");printf("%d",f);printed=1;v/=f;}f++;}
    printf("\n");
}
