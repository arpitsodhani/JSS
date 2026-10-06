#include <stdio.h>

int count_lowercase_odd_ascii(char* txt) {
    int count = 0;
    for (int i = 0; txt[i] != '\0' && txt[i] != '\n'; i++) {
        if (txt[i] >= 'a' && txt[i] <= 'z') {
            if (txt[i] % 2 == 1) {
                count++;
            }
        }
    }
    return count;
}

int main() {
    char txt[10000];
    fgets(txt, 10000, stdin);
    
    int has_space = 0;
    for (int i = 0; txt[i] != '\0' && txt[i] != '\n'; i++) {
        if (txt[i] == ' ') {
            has_space = 1;
            break;
        }
    }
    
    int has_comma = 0;
    for (int i = 0; txt[i] != '\0' && txt[i] != '\n'; ++i) if (txt[i] == ',') has_comma = 1;
    if (has_space || has_comma) {
        int first = 1;
        char word[1000];
        int idx = 0;
        
        for (int i = 0; txt[i] != '\0' && txt[i] != '\n'; i++) {
            if (txt[i] == ' ' || (!has_space && txt[i] == ',')) {
                if (idx > 0) {
                    word[idx] = '\0';
                    if (!first) printf("\n");
                    printf("%s", word);
                    first = 0;
                    idx = 0;
                }
            } else {
                word[idx++] = txt[i];
            }
        }
        if (idx > 0) {
            word[idx] = '\0';
            if (!first) printf("\n");
            printf("%s", word);
        }
        printf("\n");
    } else {
        printf("%d\n", count_lowercase_odd_ascii(txt));
    }
    
    return 0;
}
