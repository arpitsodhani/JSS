#include <stdio.h>
#include <stdlib.h>

void read_input(int *n,int *P) {
scanf("%d", n); for(int i=1;i<=*n;i++) scanf("%d", &P[i]);
}

void bit_add(int n,int *bit,int idx,int val) {
for(int i=idx;i<=n;i+=i&-i) bit[i]+=val;
}

int bit_sum(int *bit,int idx) {
int s=0; for(int i=idx;i>0;i-=i&-i) s+=bit[i]; return s;
}

int bit_kth(int n,int *bit,int k) {
int idx=0; int bitmask=1; while(bitmask<=n) bitmask<<=1; bitmask>>=1;
int cur=0; for(int d=bitmask; d>0; d>>=1){ int next=idx+d; if(next<=n && cur+bit[next]<k){ idx=next; cur+=bit[next]; } }
return idx+1;
}

void build_result(int n,int *P,int *ans) {
int *bit=(int*)calloc((size_t)(n+2),sizeof(int));
for(int i=1;i<=n;i++) bit_add(n,bit,i,1);
for(int i=n;i>=1;i--){
  int pos=bit_kth(n,bit,P[i]);
  ans[pos]=i; bit_add(n,bit,pos,-1);
}
free(bit);
}

void print_ans(int n,int *ans) {
for(int i=1;i<=n;i++){ if(i>1) printf(" "); printf("%d", ans[i]); } printf("\n");
}

int main(void){ int n; static int P[200005],ans[200005]; read_input(&n,P); build_result(n,P,ans); print_ans(n,ans); return 0; }
