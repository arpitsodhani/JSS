#include <stdio.h>

long long read_input() { long long h; scanf("%lld", &h); return h; }

long long growth(int day) { long long h = 0; for(int i = 0; i <= day; i++) { h += (1LL << i); } return h; }

int find_day(long long h) { int day = 0; while(growth(day) <= h) day++; return day; }

int main() { long long h = read_input(); printf("%d\n", find_day(h)); return 0; }
