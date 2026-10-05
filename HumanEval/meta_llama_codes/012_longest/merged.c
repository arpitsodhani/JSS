#include <stdio.h>
#include <string.h>

int find_longest(char strs[][1000], int n) {
    int max_len = 0;
    int max_idx = -1;
    for (int i = 0; i < n; i++) {
        int len = strlen(strs[i]);
        if (len > max_len) {
            max_len = len;
            max_idx = i;
        }
    }
    return max_idx;
}

int main(void) {
    int n;
    scanf("%d", &n);
    getchar();
    char strs[n][1000];
    for (int i = 0; i < n; i++) {
        fgets(strs[i], sizeof(strs[i]), stdin);
        strs[i][strcspn(strs[i], "\n")] = 0;
    }
    int idx = find_longest(strs, n);
    if (idx >= 0) {
        printf("%s\n", strs[idx]);
    } else {
        printf("None\n");
    }
    return 0;
}
