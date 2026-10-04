#include <stdio.h>

int read_input(long long *A) {
int n; scanf("%d", &n); for(int i=0;i<n;i++) scanf("%lld", &A[i]); return n;
}

int is_geo(int n,long long *A) {
if(n<=2) return 1;
for(int i=2;i<n;i++){
  if(A[i-1]*A[i-1]!=A[i-2]*A[i]) return 0;
}
return 1;
}

void print_yesno(int x) {
printf("%s\n", x?"Yes":"No");
}

int main(void){ static long long A[200005]; int n=read_input(A); int ok=is_geo(n,A); print_yesno(ok); return 0;}
