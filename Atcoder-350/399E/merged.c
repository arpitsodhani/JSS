#include <stdio.h>
#include <string.h>

void read_input(int *n, char *s, char *t) {
scanf("%d", n); scanf("%s", s); scanf("%s", t);
}

int min_ops(int n, const char *s, const char *t) {
int to[26];
for(int i=0;i<26;i++) to[i]=-1;
for(int i=0;i<n;i++){
  int a=s[i]-'a'; int b=t[i]-'a';
  if(to[a]==-1) to[a]=b;
  else if(to[a]!=b) return -1;
}
for(int i=0;i<26;i++) if(to[i]==-1) to[i]=i;
int usedT[26]={0};
for(int i=0;i<n;i++) usedT[t[i]-'a']=1;
int free_letter=-1;
for(int i=0;i<26;i++) if(!usedT[i]){ free_letter=i; break; }
int edges=0;
for(int i=0;i<26;i++) if(to[i]!=i) edges++;
int vis[26]={0};
int cycles=0;
for(int i=0;i<26;i++) if(!vis[i]){
  int x=i;
  while(!vis[x]){ vis[x]=i+1; x=to[x]; }
  if(vis[x]==i+1){
    int len=1; int y=to[x];
    while(y!=x){ len++; y=to[y]; }
    if(len>1) cycles++;
  }
}
if(cycles>0 && free_letter==-1) return -1;
return edges + cycles;
}

int main(void){ int n; static char s[200005],t[200005]; read_input(&n,s,t); int ans=min_ops(n,s,t); printf("%d\n", ans); return 0; }
