#include <stdio.h>

int is_vowel(char c) {
    c = (c >= 'a' && c <= 'z') ? c : (c + 32);
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

int count_consonants(char* word) {
    int count = 0;
    for (int i = 0; word[i] != '\0'; i++) {
        if ((word[i] >= 'a' && word[i] <= 'z') || (word[i] >= 'A' && word[i] <= 'Z')) {
            if (!is_vowel(word[i])) {
                count++;
            }
        }
    }
    return count;
}

int main() {
    char s[10000];
    int n;
    scanf("%d", &n);
    getchar();
    fgets(s, 10000, stdin);
    
    char words[1000][100];
    int word_count = 0;
    int idx = 0;
    
    for (int i = 0; s[i] != '\0' && s[i] != '\n'; i++) {
        if (s[i] == ' ') {
            words[word_count][idx] = '\0';
            if (idx > 0) word_count++;
            idx = 0;
        } else {
            words[word_count][idx++] = s[i];
        }
    }
    if (idx > 0) {
        words[word_count][idx] = '\0';
        word_count++;
    }
    
    printf("[");
    int first = 1;
    for (int i = 0; i < word_count; i++) {
        if (count_consonants(words[i]) == n) {
            if (!first) printf(", ");
            printf("\"%s\"", words[i]);
            first = 0;
        }
    }
    printf("]\n");
    
    return 0;
}
