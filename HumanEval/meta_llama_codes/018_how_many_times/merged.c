#include <stdio.h>
#include <string.h>

int count_occurrences(char *str, char *substr) {
    int count = 0;
    int substr_len = strlen(substr);
    int str_len = strlen(str);
    
    for (int i = 0; i <= str_len - substr_len; i++) {
        int match = 1;
        for (int j = 0; j < substr_len; j++) {
            if (str[i + j] != substr[j]) {
                match = 0;
                break;
            }
        }
        if (match) count++;
    }
    return count;
}

int main(void) {
    char str[1000], substr[1000];
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = 0;
    fgets(substr, sizeof(substr), stdin);
    substr[strcspn(substr, "\n")] = 0;
    int result = count_occurrences(str, substr);
    printf("%d\n", result);
    return 0;
}
