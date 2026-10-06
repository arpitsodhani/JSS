#include <stdio.h>

void compute_rounded_avg(int n, int m, char *result) {
    if (n > m) {
        strcpy(result, "-1");
        return;
    }
    long long total = (long long)n + m;
    int avg = (int)(total / 2);
    if (total % 2 != 0 && (avg & 1)) ++avg;
    result[0] = '\0';
    int temp = avg;
    int len = 0;
    if (temp == 0) {
        strcpy(result, "0b0");
        return;
    }
    char binary[100];
    while (temp > 0) {
        binary[len++] = (temp % 2) + '0';
        temp /= 2;
    }
    strcpy(result, "0b");
    for (int i = len - 1; i >= 0; i--) {
        int pos = strlen(result);
        result[pos] = binary[i];
        result[pos + 1] = '\0';
    }
}

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);
    char result[100];
    compute_rounded_avg(n, m, result);
    printf("%s\n", result);
    return 0;
}
