#include <stdio.h>

int filter_count_integers(char strs[][100], int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        int is_int = 1;
        if (strs[i][0] == '\0') {
            is_int = 0;
        } else {
            int start = 0;
            if (strs[i][0] == '-' || strs[i][0] == '+') start = 1;
            if (strs[i][start] == '\0') is_int = 0;
            for (int j = start; strs[i][j]; j++) {
                if (!isdigit(strs[i][j])) {
                    is_int = 0;
                    break;
                }
            }
        }
        if (is_int) count++;
    }
    return count;
}

int main(void) {
    int n;
    scanf("%d", &n);
    getchar();
    char strs[n][100];
    for (int i = 0; i < n; i++) {
        fgets(strs[i], sizeof(strs[i]), stdin);
        strs[i][strcspn(strs[i], "\n")] = 0;
    }
    int result = filter_count_integers(strs, n);
    printf("%d\n", result);
    return 0;
}
