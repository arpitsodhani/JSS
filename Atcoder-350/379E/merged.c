#include <stdio.h>
#include <string.h>

void read_input(char *S){ scanf("%s", S); }

long long accumulate_sum(char *S){ long long ans=0,cur=0; for(int i=0; S[i]; i++){ int d=S[i]-'0'; cur = cur*10 + (long long)d*(i+1); ans += cur; } return ans; }

void print_answer(long long ans){ printf("%lld\n", ans); }

int main(void){ char S[300000]; read_input(S); long long ans=accumulate_sum(S); print_answer(ans); return 0; }
