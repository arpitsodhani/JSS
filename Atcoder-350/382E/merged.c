#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int *X,int **P){ scanf("%d%d", N,X); *P=(int*)malloc((size_t)(*N)*sizeof(int)); for(int i=0;i<*N;i++) scanf("%d", &(*P)[i]); }

void init_prob(int N,double *prob){ for(int i=0;i<=N;i++) prob[i]=0.0; prob[0]=1.0; }

void update_prob(int i,int *P,double *prob){
    double p=P[i]/100.0;
    for(int k=i+1;k>=0;k--){
        double keep = prob[k]*(1.0-p);
        double add = (k>0? prob[k-1]*p : 0.0);
        prob[k]=keep+add;
    }
}

void build_distribution(int N,int *P,double *prob){
    init_prob(N,prob);
    for(int i=0;i<N;i++) update_prob(i,P,prob);
}

double safe_expect(double num,double den){ if(den<1e-12) return 0.0; return num/den; }

double compute_expectation(int N,int X,double *prob){
    double *E=(double*)malloc((size_t)(X+1)*sizeof(double));
    E[X]=0.0;
    for(int x=X-1; x>=0; x--){
        double p0=prob[0];
        double sum=1.0;
        for(int k=1;k<=N;k++){
            int nx = x+k; if(nx>X) nx=X;
            sum += prob[k]*E[nx];
        }
        E[x]=safe_expect(sum,1.0-p0);
    }
    double ans=E[0];
    free(E);
    return ans;
}

void print_answer(double ans){ printf("%.10f\n", ans); }

int main(void){ int N,X; int *P=NULL; read_input(&N,&X,&P); double *prob=(double*)malloc((size_t)(N+1)*sizeof(double)); build_distribution(N,P,prob); double ans=compute_expectation(N,X,prob); print_answer(ans); free(P); free(prob); return 0; }
