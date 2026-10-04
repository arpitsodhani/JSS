#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

void compare_one(const char *a, const char *b, char *result) {
    char a_copy[100], b_copy[100];
    strcpy(a_copy, a);
    strcpy(b_copy, b);
    
    for (int i = 0; a_copy[i]; i++) {
        if (a_copy[i] == ',') a_copy[i] = '.';
    }
    for (int i = 0; b_copy[i]; i++) {
        if (b_copy[i] == ',') b_copy[i] = '.';
    }
    
    double val_a = atof(a_copy);
    double val_b = atof(b_copy);
    
    if (val_a > val_b) {
        strcpy(result, a);
    } else if (val_b > val_a) {
        strcpy(result, b);
    } else {
        strcpy(result, "None");
    }
}

int main() {
    char a[100], b[100];
    fgets(a, sizeof(a), stdin);
    a[strcspn(a, "\n")] = 0;
    fgets(b, sizeof(b), stdin);
    b[strcspn(b, "\n")] = 0;
    
    char result[100];
    compare_one(a, b, result);
    printf("%s\n", result);
    return 0;
}
