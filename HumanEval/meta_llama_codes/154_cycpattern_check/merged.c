#include <stdio.h>
#include <string.h>

int check_cyclic_pattern(char* a, char* b) {
    int len_a = strlen(a);
    int len_b = strlen(b);
    
    if (len_b > len_a) return 0;
    
    
    for (int rot = 0; rot < len_b; rot++) {
        char rotated[1000];
        for (int i = 0; i < len_b; i++) {
            rotated[i] = b[(rot + i) % len_b];
        }
        rotated[len_b] = '\0';
        
        
        if (strstr(a, rotated) != NULL) {
            return 1;
        }
    }
    
    return 0;
}

int main() {
    char a[1000], b[1000];
    scanf("%s %s", a, b);
    
    if (check_cyclic_pattern(a, b)) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    
    return 0;
}
