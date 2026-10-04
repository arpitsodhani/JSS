#include <stdio.h>
#include <stdlib.h>

char* read_input(int *n, int *len) {
scanf("%d", n);
int L=1; for(int i=0;i<*n;i++) L*=3; *len=L;
char *s=(char*)malloc((size_t)L+5);
scanf("%s", s);
return s;
}

void init_costs(const char *s, int len, int **c0, int **c1) {
*c0=(int*)malloc((size_t)len*sizeof(int));
*c1=(int*)malloc((size_t)len*sizeof(int));
for(int i=0;i<len;i++){
  (*c0)[i]=(s[i]=='0')?0:1;
  (*c1)[i]=(s[i]=='1')?0:1;
}
}

void reduce_level(int len, int *c0, int *c1) {
int newlen=len/3;
for(int i=0;i<newlen;i++){
  int a0=c0[3*i], a1=c1[3*i];
  int b0=c0[3*i+1], b1=c1[3*i+1];
  int d0=c0[3*i+2], d1=c1[3*i+2];
  int best0=1e9, best1=1e9;
  int v[3][2]={{a0,a1},{b0,b1},{d0,d1}};
  for(int m=0;m<8;m++){
    int z=0, sum=0;
    for(int t=0;t<3;t++){ int bit=(m>>t)&1; if(bit==0) z++; sum+=v[t][bit]; }
    if(z>=2 && sum<best0) best0=sum;
    if(z<=1 && sum<best1) best1=sum;
  }
  c0[i]=best0; c1[i]=best1;
}
}

int solve_min_flips(int n, const char *s, int len) {
int *c0=0,*c1=0; init_costs(s,len,&c0,&c1);
int L=len; for(int level=0; level<n; level++){ reduce_level(L,c0,c1); L/=3; }
int cur = (s[0]=='0')?0:1; // original root value
int ans = (cur==0)?c1[0]:c0[0];
free(c0); free(c1); return ans;
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ int n,len; char *s=read_input(&n,&len); int ans=solve_min_flips(n,s,len); print_int(ans); free(s); return 0; }
