#include <stdio.h>

void concatenate_strings(char strs[][1000], int n, char *result) {
    result[0] = '\0';
    for (int i = 0; i < n; i++) {
        strcat(result, strs[i]);
    }
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
    char result[10000] = "";
    concatenate_strings(strs, n, result);
    printf("%s\n", result);
    return 0;
}
