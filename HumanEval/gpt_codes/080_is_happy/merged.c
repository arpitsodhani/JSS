#include <stdio.h>
#include <string.h>

int main(void) {
    char data[1001];
    scanf("%s", data);
    int cnt = strlen(data);
    if (cnt < 3) {
        printf("False\n");
        return 0;
    }
    for (int a = 0; a < cnt - 2; a++) {
        if (data[a] == data[a+1] || data[a] == data[a+2] || data[a+1] == data[a+2]) {
            printf("False\n");
            return 0;
        }
    }
    printf("True\n");
    return 0;
}
