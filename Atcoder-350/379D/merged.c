#include <stdio.h>
#include <stdlib.h>

void read_q(int *Q){ scanf("%d", Q); }

void process_queries(int Q){
    long long *arr=(long long*)malloc((size_t)Q*sizeof(long long));
    int n=0;
    long long offset=0;
    for(int i=0;i<Q;i++){
        int t; scanf("%d", &t);
        if(t==1){
            arr[n++]=-offset;
        } else if(t==2){
            long long T; scanf("%lld", &T); offset+=T;
        } else {
            long long H; scanf("%lld", &H);
            long long thresh = H - offset;
            int write=0; long long cnt=0;
            for(int j=0;j<n;j++){
                if(arr[j]>=thresh) cnt++;
                else arr[write++]=arr[j];
            }
            n=write;
            printf("%lld\n", cnt);
        }
    }
    free(arr);
}

int main(void){ int Q; read_q(&Q); process_queries(Q); return 0; }
