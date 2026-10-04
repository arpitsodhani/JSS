#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int compute_mex_from_set(int *values, int count) {
    int present[1005] = {0};
    for (int i = 0; i < count; i++) {
        if (values[i] < 1005) present[values[i]] = 1;
    }
    for (int i = 0; i < 1005; i++) {
        if (!present[i]) return i;
    }
    return count;
}

int calculate_grundy_number(int n, int *moves, int move_count, int *memo) {
    if (n == 0) return 0;
    if (memo[n] != -1) return memo[n];
    
    int reachable[1005], count = 0;
    for (int i = 0; i < move_count; i++) {
        if (n >= moves[i]) {
            reachable[count++] = calculate_grundy_number(n - moves[i], moves, move_count, memo);
        }
    }
    
    memo[n] = compute_mex_from_set(reachable, count);
    return memo[n];
}

int evaluate_nim_game_positions(int *piles, int pile_count, int *moves, int move_count) {
    int memo[1005];
    for (int i = 0; i < 1005; i++) memo[i] = -1;
    
    int xor_sum = 0;
    for (int i = 0; i < pile_count; i++) {
        xor_sum ^= calculate_grundy_number(piles[i], moves, move_count, memo);
    }
    return xor_sum != 0;
}

int main() {
    int n, m, piles[105], moves[105];
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++) {
        scanf("%d", &piles[i]);
    }
    for (int i = 0; i < m; i++) {
        scanf("%d", &moves[i]);
    }
    
    printf("%s\n", evaluate_nim_game_positions(piles, n, moves, m) ? "FIRST" : "SECOND");
    return 0;
}