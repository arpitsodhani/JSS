#include <stdio.h>

int is_prime_helper(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int largest_prime_factor(int n) {
    int largest = -1;
    for (int i = 2; i <= n; i++) {
        if (n % i == 0 && is_prime_helper(i)) {
            largest = i;
        }
    }
    return largest;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", largest_prime_factor(n));
    return 0;
}

int prime_helper(int n) {
    if(n<2) return 0;
    for(int i=2;i*i<=n;i++) if(n%i==0) return 0;
    return 1;
}

int lpf(int n) {
    int best=-1;
    for(int i=2;i<=n;i++) if(n%i==0&&prime_helper(i)) best=i;
    return best;
}

int is_prime_check(int v) {
    if(v<=1) return 0;
    int d=2;
    while(d*d<=v){if(v%d==0)return 0;d++;}
    return 1;
}

int max_prime_factor(int n) {
    int largest=-1;
    int f=2;
    while(f<=n){if(n%f==0&&is_prime_check(f))largest=f;f++;}
    return largest;
}

int test_prime(int x) {
    if(x<2) return 0;
    for(int k=2;(long long)k*k<=x;k++) if(x%k==0) return 0;
    return 1;
}

int biggest_prime_factor(int n) {
    int big=-1;
    for(int p=2;p<=n;p++) if(n%p==0&&test_prime(p)) big=p;
    return big;
}

int primality_test(int n) {
    if(n<2) return 0;
    for(int i=2;i*i<=n;i++) if(n%i==0) return 0;
    return 1;
}

int greatest_prime_factor(int n) {
    int res=-1;
    int i=2;
    while(i<=n){if(n%i==0&&primality_test(i))res=i;i++;}
    return res;
}
