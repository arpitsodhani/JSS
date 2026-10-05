#include <stdio.h>

void compute_rounded_avg(int n, int m, char *result) {
    if (n > m) {
        strcpy(result, "-1");
        return;
    }
    int sum = 0;
    for (int i = n; i <= m; i++) {
        sum += i;
    }
    int avg = (sum + (m - n + 1) / 2) / (m - n + 1);
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
