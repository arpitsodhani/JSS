#include <stdio.h>
#include <string.h>

int main(void) {
    int n;
    char substr[100];
    scanf("%d", &n);
    getchar();
    fgets(substr, sizeof(substr), stdin);
    substr[strcspn(substr, "\n")] = 0;
    for (int i = 0; i < n; i++) {
        char str[100];
        fgets(str, sizeof(str), stdin);
        str[strcspn(str, "\n")] = 0;
        if (strstr(str, substr) != NULL) {
            printf("%s\n", str);
        }
    }
    return 0;
}
