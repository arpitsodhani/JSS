#include <stdio.h>
#include <string.h>

int total_length_compare(char strs1[][1000], int n1, char strs2[][1000], int n2) {
    int len1 = 0, len2 = 0;
    for (int i = 0; i < n1; i++) {
        len1 += strlen(strs1[i]);
    }
    for (int i = 0; i < n2; i++) {
        len2 += strlen(strs2[i]);
    }
    return len1 <= len2 ? 1 : 2;
}

int main(void) {
    int n1, n2;
    scanf("%d", &n1);
    getchar();
    char strs1[n1][1000];
    for (int i = 0; i < n1; i++) {
        fgets(strs1[i], sizeof(strs1[i]), stdin);
        strs1[i][strcspn(strs1[i], "\n")] = 0;
    }
    scanf("%d", &n2);
    getchar();
    char strs2[n2][1000];
    for (int i = 0; i < n2; i++) {
        fgets(strs2[i], sizeof(strs2[i]), stdin);
        strs2[i][strcspn(strs2[i], "\n")] = 0;
    }
    int choice = total_length_compare(strs1, n1, strs2, n2);
    if (choice == 1) {
        for (int i = 0; i < n1; i++) {
            printf("%s", strs1[i]);
            if (i < n1 - 1) printf(" ");
        }
    } else {
        for (int i = 0; i < n2; i++) {
            printf("%s", strs2[i]);
            if (i < n2 - 1) printf(" ");
        }
    }
    printf("\n");
    return 0;
}
