#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void initialize_dp_table(int max_sweet, int max_salty, int dp[3005][3005]) {
    for (int i = 0; i <= max_sweet; i++) {
        for (int j = 0; j <= max_salty; j++) {
            dp[i][j] = 0;
        }
    }
}

int check_budget_constraints(int current_sweet, int current_salty, int dish_sweet, int dish_salty, int max_sweet, int max_salty) {
    return (current_sweet >= dish_sweet && current_salty >= dish_salty);
}

void update_dp_state_with_dish(int max_sweet, int max_salty, int dp[3005][3005], int dish_sweet, int dish_salty) {
    for (int i = max_sweet; i >= dish_sweet; i--) {
        for (int j = max_salty; j >= dish_salty; j--) {
            int new_count = dp[i - dish_sweet][j - dish_salty] + 1;
            if (new_count > dp[i][j]) {
                dp[i][j] = new_count;
            }
        }
    }
}

int execute_knapsack_optimization(int n, int max_sweet, int max_salty, int *sweetness, int *saltiness) {
    int dp[3005][3005];
    initialize_dp_table(max_sweet, max_salty, dp);
    for (int dish = 0; dish < n; dish++) {
        update_dp_state_with_dish(max_sweet, max_salty, dp, sweetness[dish], saltiness[dish]);
    }
    return dp[max_sweet][max_salty];
}

int main() {
    int n, x, y;
    int sweetness[305], saltiness[305];
    scanf("%d %d %d", &n, &x, &y);
    for (int i = 0; i < n; i++) scanf("%d %d", &sweetness[i], &saltiness[i]);
    printf("%d\n", execute_knapsack_optimization(n, x, y, sweetness, saltiness));
    return 0;
}