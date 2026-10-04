#include <stdio.h>

int modp(int n, int p) {
    int result = 1;
    for (int i = 0; i < n; i++) {
        result = (result * 2) % p;
    }
    return result;
}

int main() {
    int n, p;
    scanf("%d %d", &n, &p);
    printf("%d\n", modp(n, p));
    return 0;
}

int mod_power2(int n, int p) {
    int res=1;
    for(int i=0;i<n;i++) res=(res*2)%p;
    return res;
}

int two_pow_mod(int exp, int mod) {
    int val=1;
    int i=0;
    while(i<exp){val=(val*2)%mod;i++;}
    return val;
}

int power_mod(int n, int m) {
    int r=1;
    for(int k=0;k<n;k++) r=(r*2)%m;
    return r;
}

int modular_exp(int n, int p) {
    int x=1;
    for(int i=n;i>0;i--) x=(x*2)%p;
    return x;
}
