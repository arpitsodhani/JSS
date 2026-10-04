#include <stdio.h>

void read_cards(int *a) {
for(int i=0;i<7;i++) scanf("%d", &a[i]);
}

int is_fullhouse(const int *a) {
int vals[7]; int cnt[7]; int m=0;
for(int i=0;i<7;i++){
  int x=a[i]; int j=0; for(;j<m;j++) if(vals[j]==x) break;
  if(j==m){ vals[m]=x; cnt[m]=0; m++; }
  cnt[j]++;
}
for(int i=0;i<m;i++) for(int j=0;j<m;j++) if(i!=j){
  if(cnt[i]>=3 && cnt[j]>=2) return 1;
}
return 0;
}

void print_yesno(int ok) {
puts(ok?"Yes":"No");
}

int main(void){ int a[7]; read_cards(a); int ok=is_fullhouse(a); print_yesno(ok); return 0; }
