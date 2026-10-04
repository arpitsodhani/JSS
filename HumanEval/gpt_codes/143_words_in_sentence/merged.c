#include <stdio.h>
#include <string.h>

int is_prime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    char sentence[10000];
    fgets(sentence, 10000, stdin);
    
    char words[1000][100];
    int word_count = 0;
    int idx = 0;
    
    for (int i = 0; sentence[i] != '\0' && sentence[i] != '\n'; i++) {
        if (sentence[i] == ' ') {
            if (idx > 0) {
                words[word_count][idx] = '\0';
                word_count++;
                idx = 0;
            }
        } else {
            words[word_count][idx++] = sentence[i];
        }
    }
    if (idx > 0) {
        words[word_count][idx] = '\0';
        word_count++;
    }
    
    int first = 1;
    for (int i = 0; i < word_count; i++) {
        int len = strlen(words[i]);
        if (is_prime(len)) {
            if (!first) printf(" ");
            printf("%s", words[i]);
            first = 0;
        }
    }
    printf("\n");
    
    return 0;
}
