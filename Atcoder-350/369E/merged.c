#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compute_operation_cost(int insert_cost, int delete_cost, int replace_cost) {
    int min_cost = insert_cost;
    if (delete_cost < min_cost) min_cost = delete_cost;
    if (replace_cost < min_cost) min_cost = replace_cost;
    return min_cost;
}

void initialize_edit_distance_table(int dp[1005][1005], int len1, int len2) {
    for (int i = 0; i <= len1; i++) dp[i][0] = i;
    for (int j = 0; j <= len2; j++) dp[0][j] = j;
}

int compute_edit_distance(char *s1, char *s2) {
    int len1 = strlen(s1), len2 = strlen(s2);
    int dp[1005][1005];
    initialize_edit_distance_table(dp, len1, len2);
    
    for (int i = 1; i <= len1; i++) {
        for (int j = 1; j <= len2; j++) {
            if (s1[i-1] == s2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                int insert = dp[i][j-1] + 1;
                int delete = dp[i-1][j] + 1;
                int replace = dp[i-1][j-1] + 1;
                dp[i][j] = compute_operation_cost(insert, delete, replace);
            }
        }
    }
    return dp[len1][len2];
}

int main() {
    char s1[1005], s2[1005];
    scanf("%s %s", s1, s2);
    printf("%d\n", compute_edit_distance(s1, s2));
    return 0;
}