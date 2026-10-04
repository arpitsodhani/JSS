#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int check_if_last_char_is_a_letter(const char *txt) {
    int len = strlen(txt);
    if (len == 0) return 0;
    
    char last = txt[len - 1];
    if (!isalpha(last)) return 0;
    
    if (len == 1) return 1;
    
    if (txt[len - 2] == ' ') return 1;
    
    return 0;
}

int main() {
    char txt[10000];
    fgets(txt, sizeof(txt), stdin);
    txt[strcspn(txt, "\n")] = 0;
    printf("%s\n", check_if_last_char_is_a_letter(txt) ? "True" : "False");
    return 0;
}
