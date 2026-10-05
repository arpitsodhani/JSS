#include <stdio.h>
#include <string.h>

int have_same_chars(const char *s1, const char *s2) {
    int seen1[256] = {0}, seen2[256] = {0};
    for (int i = 0; s1[i]; i++) {
        seen1[(unsigned char)s1[i]] = 1;
    }
    for (int i = 0; s2[i]; i++) {
        seen2[(unsigned char)s2[i]] = 1;
    }
    for (int i = 0; i < 256; i++) {
        if (seen1[i] != seen2[i]) {
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
