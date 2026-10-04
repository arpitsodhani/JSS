

#include <stdio.h>
#include <stdlib.h>
int dsum(int n) {
    int s=0, neg=(n<0); if(neg) n=-n;
    char b[20]; sprintf(b,"%d",n);
    for(int i=0; b[i]; i++) { int d=b[i]-'0'; s+=(i==0&&neg)?-d:d; }
    return s;
}
int main() {
    int n, a[100]; scanf("%d", &n);
    for(int i=0; i<n; i++) scanf("%d", &a[i]);
    for(int i=0; i<n-1; i++)
        for(int j=i+1; j<n; j++)
            if(dsum(a[i])>dsum(a[j])) { int t=a[i]; a[i]=a[j]; a[j]=t; }
    for(int i=0; i<n; i++) printf("%d%c", a[i], i<n-1?' ':'\\n');
    return 0;
}
