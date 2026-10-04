#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void initialize_selection_dp(int max_k, long long *dp) {
    for (int i = 0; i <= max_k; i++) {
        dp[i] = -1e18;
    }
    dp[0] = 0;
}

void update_selection_state(int max_k, long long *dp, int element) {
    for (int selected = max_k; selected >= 1; selected--) {
        long long new_value = dp[selected - 1] + element;
        if (new_value > dp[selected]) {
            dp[selected] = new_value;
        }
    }
}

long long optimize_k_element_selection(int n, int k, int *array) {
    long long dp[100005];
    initialize_selection_dp(k, dp);
    for (int i = 0; i < n; i++) {
        update_selection_state(k, dp, array[i]);
    }
    return dp[k];
}

int main() {
    int n, k, array[100005];
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++) scanf("%d", &array[i]);
    printf("%lld\n", optimize_k_element_selection(n, k, array));
    return 0;
}