#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void total_match(char** lst1, int n1, char** lst2, int n2, char*** result, int* result_n) {
    int len1 = 0, len2 = 0;
    for (int i = 0; i < n1; i++) len1 += strlen(lst1[i]);
    for (int i = 0; i < n2; i++) len2 += strlen(lst2[i]);
    if (len1 <= len2) {
        *result = lst1;
        *result_n = n1;
    } else {
        *result = lst2;
        *result_n = n2;
    }
}

int main() {
    int n1, n2;
    scanf("%d", &n1);
    char* lst1[n1];
    char buffer1[100][100];
    for (int i = 0; i < n1; i++) {
        scanf("%s", buffer1[i]);
        lst1[i] = buffer1[i];
    }
    scanf("%d", &n2);
    char* lst2[n2];
    char buffer2[100][100];
    for (int i = 0; i < n2; i++) {
        scanf("%s", buffer2[i]);
        lst2[i] = buffer2[i];
    }
    char** result;
    int result_n;
    total_match(lst1, n1, lst2, n2, &result, &result_n);
    for (int i = 0; i < result_n; i++) {
        if (i > 0) printf(" ");
        printf("%s", result[i]);
    }
    printf("\n");
    return 0;
}

