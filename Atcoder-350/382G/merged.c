#include <stdio.h>
#include <stdlib.h>

void read_input(long long *K,long long *sx,long long *sy,long long *tx,long long *ty){ scanf("%lld%lld%lld%lld%lld", K,sx,sy,tx,ty); }

long long approx_distance(long long K,long long sx,long long sy,long long tx,long long ty){
    long long dx = sx>tx? sx-tx: tx-sx;
    long long dy = sy>ty? sy-ty: ty-sy;
    long long d = dx + dy;
    long long ans = d / K;
    if(d % K) ans++;
    return ans;
}

void print_answer(long long ans){ printf("%lld\n", ans); }

int main(void){ long long K,sx,sy,tx,ty; read_input(&K,&sx,&sy,&tx,&ty); long long ans=approx_distance(K,sx,sy,tx,ty); print_answer(ans); return 0; }
