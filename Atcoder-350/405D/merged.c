#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmp_u32(const void *a, const void *b) {
int cmp_u32(const void*a,const void*b){ unsigned x=*(const unsigned*)a, y=*(const unsigned*)b; return (x>y)-(x<y); }
}

unsigned h32(unsigned x){ x^=x>>16; x*=0x7feb352dU; x^=x>>15; x*=0x846ca68bU; x^=x>>16; return x; }

void solve(void){ int N; scanf("%d", &N); unsigned *m=(unsigned*)malloc((size_t)N*sizeof(unsigned)); for(int i=0;i<N;i++){ char s[16]; scanf("%10s", s); unsigned mask=0; for(int k=0;s[k];k++) mask |= 1u<<(s[k]-'a'); m[i]=mask; } qsort(m,N,sizeof(unsigned),cmp_u32); unsigned *uniq=(unsigned*)malloc((size_t)N*sizeof(unsigned)); int *cnt=(int*)malloc((size_t)N*sizeof(int)); int D=0; for(int i=0;i<N;){ int j=i+1; while(j<N && m[j]==m[i]) j++; uniq[D]=m[i]; cnt[D]=j-i; D++; i=j; }
  int cap=1; while(cap < D*256) cap<<=1; int maskh=cap-1; unsigned *hkey=(unsigned*)malloc((size_t)cap*sizeof(unsigned)); int *hval=(int*)malloc((size_t)cap*sizeof(int)); unsigned char *used=(unsigned char*)malloc((size_t)cap); memset(used,0,(size_t)cap);
  for(int i=0;i<D;i++){ unsigned mm=uniq[i]; int c=cnt[i]; for(unsigned sub=mm; sub; sub=(sub-1)&mm){ unsigned idx=h32(sub)&(unsigned)maskh; while(used[idx] && hkey[idx]!=sub) idx=(idx+1)&(unsigned)maskh; if(!used[idx]){ used[idx]=1; hkey[idx]=sub; hval[idx]=c; } else hval[idx]+=c; } }
  long long ordered=0; for(int i=0;i<D;i++){ unsigned mm=uniq[i]; int c=cnt[i]; long long u=0; for(unsigned sub=mm; sub; sub=(sub-1)&mm){ unsigned idx=h32(sub)&(unsigned)maskh; while(used[idx] && hkey[idx]!=sub) idx=(idx+1)&(unsigned)maskh; int cc=used[idx]?hval[idx]:0; int bits=__builtin_popcount(sub); u += (bits&1)?cc:-cc; } long long dis=(long long)N-u; ordered += (long long)c*dis; }
  long long dis_pairs=ordered/2; long long total=(long long)N*(N-1)/2; printf("%lld\n", total-dis_pairs);
  free(m); free(uniq); free(cnt); free(hkey); free(hval); free(used);
}

int main(void){ solve(); return 0; }
