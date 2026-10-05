#include <stdio.h>
#include <string.h>

int have_same_chars(char *s1, char *s2) {
    int freq1[256] = {0}, freq2[256] = {0};
    for (int i = 0; s1[i]; i++) {
        freq1[(unsigned char)s1[i]]++;
    }
    for (int i = 0; s2[i]; i++) {
        freq2[(unsigned char)s2[i]]++;
    }
    for (int i = 0; i < 256; i++) {
        if (freq1[i] != freq2[i]) {
            return 0;
        }
    }
    return 1;
}

int main(void) {
    char s1[1000], s2[1000];
    fgets(s1, sizeof(s1), stdin);
    s1[strcspn(s1, "\n")] = 0;
    fgets(s2, sizeof(s2), stdin);
    s2[strcspn(s2, "\n")] = 0;
    if (have_same_chars(s1, s2)) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    return 0;
}
