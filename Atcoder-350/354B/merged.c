#include <stdio.h>

int read_input(char names[][20], int *ratings) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) scanf("%s%d", names[i], &ratings[i]); return n; }

int compare_str(char *a, char *b) { int i = 0; while(a[i] && b[i]) { if(a[i] < b[i]) return -1; if(a[i] > b[i]) return 1; i++; } if(!a[i] && b[i]) return -1; if(a[i] && !b[i]) return 1; return 0; }

void sort_lex(char names[][20], int *ratings, int n) { for(int i = 0; i < n - 1; i++) { for(int j = i + 1; j < n; j++) { if(compare_str(names[i], names[j]) > 0) { char tmp[20]; int r; for(int k = 0; k < 20; k++) tmp[k] = names[i][k]; for(int k = 0; k < 20; k++) names[i][k] = names[j][k]; for(int k = 0; k < 20; k++) names[j][k] = tmp[k]; r = ratings[i]; ratings[i] = ratings[j]; ratings[j] = r; } } } }

void find_winner(char names[][20], int *ratings, int n) { int sum = 0; for(int i = 0; i < n; i++) sum += ratings[i]; printf("%s\n", names[sum % n]); }

int main() { char names[100][20]; int ratings[100]; int n = read_input(names, ratings); sort_lex(names, ratings, n); find_winner(names, ratings, n); return 0; }
