#include <stdio.h>
#include <stdlib.h>

void read_tree(int *n, int *k, int *u, int *v) {
int N,K; scanf("%d %d", &N, &K);
*n=N*K; *k=K;
for(int i=0;i<*n-1;i++){ scanf("%d %d", &u[i], &v[i]); u[i]--; v[i]--; }
}

void add_edge(int a, int b, int *head, int *to, int *nx, int *ec) {
to[*ec]=b; nx[*ec]=head[a]; head[a]=(*ec)++;
}

int dfs_paths(int x, int p, int k, const int *head, const int *to, const int *nx, int *ok) {
int buf_sz=0;
static int buf[200005];
for(int e=head[x]; e!=-1; e=nx[e]){
  int y=to[e]; if(y==p) continue;
  int r=dfs_paths(y,x,k,head,to,nx,ok);
  if(!*ok) return -1;
  r++; if(r==k-1) continue; buf[buf_sz++]=r;
}
if(buf_sz==0) return 0;
for(int i=0;i<buf_sz;i++){
  for(int j=i+1;j<buf_sz;j++){
    if(buf[i]>buf[j]){ int t=buf[i]; buf[i]=buf[j]; buf[j]=t; }
  }
}
int used=0; int l=0,r=buf_sz-1;
int remain=-1;
while(l<=r){
  if(l==r){ remain=buf[l]; break; }
  int a=buf[l], b=buf[r];
  if(a+b==k-1){ used+=2; l++; r--; }
  else if(a+b<k-1){ l++; }
  else { r--; }
}
if(remain==-1 && used!=buf_sz) { *ok=0; return -1; }
if(remain!=-1 && used!=buf_sz-1) { *ok=0; return -1; }
return (remain==-1)?0:remain;
}

int can_decompose(int n, int k, const int *u, const int *v) {
if(k==1) return 1;
int *head=(int*)malloc((size_t)n*sizeof(int));
int *to=(int*)malloc((size_t)(2*(n-1))*sizeof(int));
int *nx=(int*)malloc((size_t)(2*(n-1))*sizeof(int));
for(int i=0;i<n;i++) head[i]=-1;
int ec=0;
for(int i=0;i<n-1;i++){
  add_edge(u[i],v[i],head,to,nx,&ec);
  add_edge(v[i],u[i],head,to,nx,&ec);
}
int ok=1;
int rem=dfs_paths(0,-1,k,head,to,nx,&ok);
int ans = ok && (rem==0);
free(head); free(to); free(nx);
return ans;
}

void print_yesno(int ok) {
puts(ok?"Yes":"No");
}

int main(void){ int n,k; static int u[200005], v[200005]; read_tree(&n,&k,u,v); int ok=can_decompose(n,k,u,v); print_yesno(ok); return 0; }
