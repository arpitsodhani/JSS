#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int is_nested(const char *string) {
    int n = strlen(string);
    int count[n + 1];
    count[0] = 0;
    
    for (int i = 0; i < n; i++) {
        count[i + 1] = count[i] + (string[i] == '[' ? 1 : -1);
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            if (count[i] == count[j]) {
                int min_depth = count[i];
                for (int k = i + 1; k < j; k++) {
                    if (count[k] < min_depth) {
                        min_depth = count[k];
                    }
                }
                if (min_depth < count[i]) {
                    return 1;
                }
            }
        }
    }
    
    return 0;
}

int main() {
    char string[10000];
    fgets(string, sizeof(string), stdin);
    string[strcspn(string, "\n")] = 0;
    printf("%s\n", is_nested(string) ? "True" : "False");
    return 0;
}
