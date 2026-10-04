#include <stdio.h>
#include <stdlib.h>

int read_input(int **K_out,int ***vals_out) {
int n; scanf("%d", &n);
int *K=(int*)malloc((size_t)n*sizeof(int));
int **vals=(int**)malloc((size_t)n*sizeof(int*));
for(int i=0;i<n;i++){
  scanf("%d", &K[i]);
  vals[i]=(int*)malloc((size_t)K[i]*sizeof(int));
  for(int j=0;j<K[i];j++) scanf("%d", &vals[i][j]);
}
*K_out=K; *vals_out=vals; return n;
}

double max_prob(int n,int *K,int **vals) {
double best=0.0;
for(int i=0;i<n;i++) for(int j=i+1;j<n;j++){
  double p=0.0;
  for(int a=0;a<K[i];a++) for(int b=0;b<K[j];b++) if(vals[i][a]==vals[j][b]) p+=1.0/((double)K[i]*(double)K[j]);
  if(p>best) best=p;
}
return best;
}

void print_double(double x) {
printf("%.10f\n", x);
}

int main(void){ int *K; int **vals; int n=read_input(&K,&vals); double ans=max_prob(n,K,vals); print_double(ans); for(int i=0;i<n;i++) free(vals[i]); free(vals); free(K); return 0; }
