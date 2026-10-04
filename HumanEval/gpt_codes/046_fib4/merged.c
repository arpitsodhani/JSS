#include <stdio.h>

int fib4(int n) {
    if (n < 2) return 0;
    if (n == 2) return 2;
    if (n == 3) return 0;
    int a = 0, b = 0, c = 2, d = 0;
    for (int i = 4; i <= n; i++) {
        int next = a + b + c + d;
        a = b; b = c; c = d; d = next;
    }
    return d;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", fib4(n));
    return 0;
}

int fib4_seq(int n) {
    if(n<2) return 0;
    if(n==2) return 2;
    if(n==3) return 0;
    int w=0,x=0,y=2,z=0;
    for(int i=4;i<=n;i++){int nxt=w+x+y+z;w=x;x=y;y=z;z=nxt;}
    return z;
}

int compute_fib4(int idx) {
    if(idx==0||idx==1||idx==3) return 0;
    if(idx==2) return 2;
    int a=0,b=0,c=2,d=0;
    int i=4;
    while(i<=idx){int nxt=a+b+c+d;a=b;b=c;c=d;d=nxt;i++;}
    return d;
}

int fib4_value(int n) {
    int f[1001];
    f[0]=0;f[1]=0;f[2]=2;f[3]=0;
    for(int i=4;i<=n;i++) f[i]=f[i-1]+f[i-2]+f[i-3]+f[i-4];
    return f[n];
}

int four_fib(int n) {
    if(n<2) return 0;
    if(n==2) return 2;
    if(n==3) return 0;
    int p=0,q=0,r=2,s=0;
    for(int k=4;k<=n;k++){int t=p+q+r+s;p=q;q=r;r=s;s=t;}
    return s;
}
