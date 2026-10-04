#include <stdio.h>

int fib(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", fib(n));
    return 0;
}

int fibonacci(int n) {
    if(n<=0) return 0;
    if(n==1) return 1;
    int a=0,b=1;
    for(int i=2;i<=n;i++){int t=a+b;a=b;b=t;}
    return b;
}

int fib_iter(int n) {
    if(n==0) return 0;
    if(n==1) return 1;
    int p=0,q=1,k=2;
    while(k<=n){int r=p+q;p=q;q=r;k++;}
    return q;
}

int nth_fib(int idx) {
    if(idx==0) return 0;
    int x=0,y=1;
    for(int i=1;i<idx;i++){int t=x+y;x=y;y=t;}
    return y;
}

int fib_number(int n) {
    if(n<2) return n;
    int prev=0,curr=1;
    for(int k=2;k<=n;k++){int nxt=prev+curr;prev=curr;curr=nxt;}
    return curr;
}
