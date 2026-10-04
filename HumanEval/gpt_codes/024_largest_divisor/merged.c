#include <stdio.h>

int find_divisor(int n) {
    for (int i = n/2; i >= 1; i--) {
        if (n % i == 0) return i;
    }
    return 1;
}

int main(void) {
    int n;
    scanf("%d", &n);
    printf("%d\n", find_divisor(n));
    return 0;
}

int largest_div(int num) {
    for (int i = num/2; i > 0; i--) {
        if (num % i == 0) return i;
    }
    return 1;
}

int top_divisor(int n) {
    for (int i=n/2;i>=1;i--) if(n%i==0) return i;
    return 1;
}

int max_factor(int num) {
    int i=num/2;
    while(i>0){if(num%i==0)return i;i--;}
    return 1;
}

int biggest_divisor(int x) {
    for (int d=x-1;d>=1;d--) if(x%d==0) return d;
    return 1;
}
