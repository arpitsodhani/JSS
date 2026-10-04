#include <stdio.h>

int read_q(long long *L) {
int Q; scanf("%d", &Q); return Q;
}

void push_snake(long long len,long long *head,long long *lenq,int *tail,int *cnt,long long *offset) {
long long h=0;
if(*cnt==0) h=0; else { int last=(*tail-1+200005)%200005; h=head[last]+lenq[last]; }
head[*tail]=h; lenq[*tail]=len; *tail=(*tail+1)%200005; (*cnt)++;
}

void pop_snake(long long *head,long long *lenq,int *headp,int *cnt,long long *offset) {
long long m=lenq[*headp]; *offset+=m; *headp=(*headp+1)%200005; (*cnt)--;
}

long long query_k(int k,long long *head,int headp,long long offset) {
int idx=(headp+k-1)%200005; return head[idx]-offset;
}

int main(void){ int Q=read_q(NULL); static long long head[200005],lenq[200005]; int headp=0,tail=0,cnt=0; long long offset=0; for(int qi=0;qi<Q;qi++){ int t; scanf("%d", &t); if(t==1){ long long l; scanf("%lld", &l); push_snake(l,head,lenq,&tail,&cnt,&offset); } else if(t==2){ pop_snake(head,lenq,&headp,&cnt,&offset); } else { int k; scanf("%d", &k); long long ans=query_k(k,head,headp,offset); printf("%lld\n", ans); } } return 0; }
