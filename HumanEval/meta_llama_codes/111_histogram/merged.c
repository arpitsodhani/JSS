#include <stdio.h>

void find_max_chars(char* test, char* result, int* result_len) {
    int count[256] = {0};
    int max_count = 0;
    
    for (int i = 0; test[i] != '\0' && test[i] != '\n'; i++) {
        if (test[i] != ' ') {
            count[(int)test[i]]++;
            if (count[(int)test[i]] > max_count) {
                max_count = count[(int)test[i]];
            }
        }
    }
    
    *result_len = 0;
    for (int i = 0; i < 256; i++) {
        if (count[i] == max_count && max_count > 0) {
            result[(*result_len)++] = (char)i;
        }
    }
}

int main() {
    char test[1000];
    fgets(test, 1000, stdin);
    
    char result[256];
    int result_len;
    find_max_chars(test, result, &result_len);
    
    for (int i = 0; i < result_len; i++) {
        if (i > 0) printf(", ");
        printf("%c ", result[i]);
        
        int count = 0;
        for (int j = 0; test[j] != '\0' && test[j] != '\n'; j++) {
            if (test[j] == result[i]) count++;
        }
        printf("%d", count);
    }
    printf("\n");
    
    return 0;
}
