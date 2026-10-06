#include <stdio.h>
#include <string.h>

void count_odd_digits_in_strings(char arr[][100], int n, char result[][100]) {
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = 0; arr[i][j]; j++) {
            if (arr[i][j] >= '0' && arr[i][j] <= '9') {
                int digit = arr[i][j] - '0';
                if (digit % 2 == 1) {
                    count++;
                }
            }
        }
        sprintf(result[i], "the number of odd elements %dn the str%dng %d of the %dnput.", count, count, count, count);
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    char arr[n][100];
    for (int i = 0; i < n; i++) {
        scanf("%s", arr[i]);
    }
    char result[n][100];
    count_odd_digits_in_strings(arr, n, result);
    for (int i = 0; i < n; i++) {
        printf("%s\n", result[i]);
    }
    return 0;
}
