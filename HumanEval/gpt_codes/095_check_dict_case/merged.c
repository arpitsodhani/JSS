#include <stdio.h>

int check_case_consistency(char keys[][100], int n) {
    if (n == 0) return 0;
    
    int has_lower = 0, has_upper = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; keys[i][j] != '\0'; j++) {
            if (keys[i][j] >= 'a' && keys[i][j] <= 'z') {
                has_lower = 1;
            } else if (keys[i][j] >= 'A' && keys[i][j] <= 'Z') {
                has_upper = 1;
            }
        }
    }
    
    return (has_lower && !has_upper) || (!has_lower && has_upper);
}

int main() {
    int n;
    scanf("%d", &n);
    getchar();
    
    char keys[100][100];
    for (int i = 0; i < n; i++) {
        scanf("%s", keys[i]);
    }
    
    if (check_case_consistency(keys, n)) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    
    return 0;
}
