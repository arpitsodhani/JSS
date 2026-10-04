#include <stdio.h>
#include <stdlib.h>

void read_nq(int *n, int *q) {
scanf("%d %d", n, q);
}

void init_maps(int n, int *nest_id, int *label_of, int *pigeon_id) {
for(int i=1;i<=n;i++){ nest_id[i]=i; label_of[i]=i; pigeon_id[i]=i; }
}

void move_pigeon(int a, int b, const int *nest_id, int *pigeon_id) {
pigeon_id[a]=nest_id[b];
}

void swap_nests(int a, int b, int *nest_id, int *label_of) {
int ida=nest_id[a], idb=nest_id[b]; nest_id[a]=idb; nest_id[b]=ida; label_of[ida]=b; label_of[idb]=a;
}

int query_pigeon(int a, const int *pigeon_id, const int *label_of) {
return label_of[pigeon_id[a]];
}

int main(void){ int n,q; read_nq(&n,&q);
int *nest_id=(int*)malloc((size_t)(n+1)*sizeof(int));
int *label_of=(int*)malloc((size_t)(n+1)*sizeof(int));
int *pigeon_id=(int*)malloc((size_t)(n+1)*sizeof(int));
init_maps(n,nest_id,label_of,pigeon_id);
for(int i=0;i<q;i++){
  int t; scanf("%d", &t);
  if(t==1){ int a,b; scanf("%d %d", &a,&b); move_pigeon(a,b,nest_id,pigeon_id); }
  else if(t==2){ int a,b; scanf("%d %d", &a,&b); swap_nests(a,b,nest_id,label_of); }
  else { int a; scanf("%d", &a); int ans=query_pigeon(a,pigeon_id,label_of); printf("%d\n", ans); }
}
free(nest_id); free(label_of); free(pigeon_id);
return 0; }
