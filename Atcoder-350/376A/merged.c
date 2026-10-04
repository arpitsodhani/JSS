#include <stdio.h>

void read_input(int *N,int *C,int *T){ scanf("%d%d", N,C); for(int i=0;i<*N;i++) scanf("%d", &T[i]); }

int count_candies(int N,int C,int *T){ int ans=0; int last=-1e9; for(int i=0;i<N;i++){ if(T[i]-last>=C){ ans++; last=T[i]; } } return ans; }

void print_answer(int ans){ printf("%d\n", ans); }

int main(void){ int N,C; int T[200005]; read_input(&N,&C,T); int ans=count_candies(N,C,T); print_answer(ans); return 0; }
