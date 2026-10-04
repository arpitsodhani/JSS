#include <stdio.h>

int fizz_buzz(int n) {
    int count = 0;
    for (int i = 1; i < n; i++) {
        if (i % 11 == 0 || i % 13 == 0) {
            int temp = i;
            while (temp > 0) {
                if (temp % 10 == 7) count++;
                temp /= 10;
            }
        }
    }
    return count;
}

int main(void) {
    int n;
    scanf("%d", &n);
    printf("%d\n", fizz_buzz(n));
    return 0;
}

int count_sevens(int limit) {
    int total = 0;
    for (int i = 1; i < limit; i++) {
        if (i % 11 == 0 || i % 13 == 0) {
            int num = i;
            while (num > 0) {
                if (num % 10 == 7) total++;
                num /= 10;
            }
        }
    }
    return total;
}

int count_digit7(int n) {
    int res=0;
    for(int i=1;i<n;i++) if(i%11==0||i%13==0){int t=i;while(t>0){if(t%10==7)res++;t/=10;}}
    return res;
}

int sevens_in_multiples(int lim) {
    int cnt=0;
    int i=1;
    while(i<lim){if(i%11==0||i%13==0){int v=i;while(v){if(v%10==7)cnt++;v/=10;}}i++;}
    return cnt;
}

int digit7_count(int bound) {
    int total=0;
    for(int k=1;k<bound;k++) if(k%11==0||k%13==0){int num=k;do{if(num%10==7)total++;num/=10;}while(num);}
    return total;
}
