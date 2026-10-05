#include <stdio.h>
#include <string.h>

int count_unique_chars(char* word) {
    int seen[256] = {0};
    int count = 0;
    
    for (int i = 0; word[i] != '\0'; i++) {
        if (!seen[(int)word[i]]) {
            seen[(int)word[i]] = 1;
            count++;
        }
    }
    
    return count;
}

int main() {
    int n;
    scanf("%d", &n);
    
    char words[1000][100];
    for (int i = 0; i < n; i++) {
        scanf("%s", words[i]);
    }
    
    int max_unique = -1;
    char max_word[100];
    
    for (int i = 0; i < n; i++) {
        int unique = count_unique_chars(words[i]);
        if (unique > max_unique || (unique == max_unique && strcmp(words[i], max_word) < 0)) {
            max_unique = unique;
            strcpy(max_word, words[i]);
        }
    }
    
    printf("%s\n", max_word);
    return 0;
}
