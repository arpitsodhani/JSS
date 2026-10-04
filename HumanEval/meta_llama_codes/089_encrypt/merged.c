#include <stdio.h>
#include <string.h>

int main(void) {
    char data[1001];
    scanf("%s", data);
    int cnt = strlen(data);
    for (int a = 0; a < cnt; a++) {
        if (data[a] >= 'a' && data[a] <= 'z') {
            data[a] = 'a' + (data[a] - 'a' + 4) % 26;
        }
    }
    printf("%s\n", data);
    return 0;
}
