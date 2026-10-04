#include <stdio.h>

int is_prime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int prime_fib(int n) {
    int a = 1, b = 2, count = 0;
    while (1) {
        if (is_prime(a)) {
            count++;
            if (count == n) return a;
        }
        int temp = a + b;
        a = b;
        b = temp;
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    printf("%d\n", prime_fib(n));
    return 0;
}

int check_prime(int num) {
    if (num <= 1) return 0;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) return 0;
    }
    return 1;
}

int find_prime_fib(int target) {
    int x = 1, y = 2, found = 0;
    while (1) {
        if (check_prime(x)) {
            found++;
            if (found == target) return x;
        }
        int next = x + y;
        x = y;
        y = next;
    }
}

int primality(int n) {
    if(n<2) return 0;
    for(int i=2;i*i<=n;i++) if(n%i==0) return 0;
    return 1;
}

int nth_prime_fib(int n) {
    int a=1,b=2,cnt=0;
    while(1){if(primality(a)){cnt++;if(cnt==n)return a;}int tmp=a+b;a=b;b=tmp;}
}

int is_prime_fib(int v) {
    if(v<=1) return 0;
    int d=2;
    while(d*d<=v){if(v%d==0)return 0;d++;}
    return 1;
}

int prime_fibonacci(int target) {
    int x=1,y=2,found=0;
    while(1){if(is_prime_fib(x)){found++;if(found==target)return x;}int nxt=x+y;x=y;y=nxt;}
}

int prime_check(int num) {
    if(num<2) return 0;
    for(int k=2;(long long)k*k<=num;k++) if(num%k==0) return 0;
    return 1;
}

int get_prime_fib(int idx) {
    int p=1,q=2,count=0;
    while(1){if(prime_check(p)){count++;if(count==idx)return p;}int r=p+q;p=q;q=r;}
}
