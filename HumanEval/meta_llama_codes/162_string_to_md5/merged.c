#include <stdio.h>
#include <string.h>

void compute_simple_hash(char* text, char* result) {
    int len = strlen(text);
    if (len == 0 || (len == 1 && text[0] == '\n')) {
        strcpy(result, "None");
        return;
    }
    
    
    unsigned long hash = 5381;
    for (int i = 0; text[i] != '\0' && text[i] != '\n'; i++) {
        hash = ((hash << 5) + hash) + text[i];
    }
    
    sprintf(result, "%032lx", hash);
}

int main() {
    char text[10000];
    fgets(text, 10000, stdin);
    
    char result[100];
    compute_simple_hash(text, result);
    
    printf("%s\n", result);
    return 0;
}
