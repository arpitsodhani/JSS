#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int strength(const char *ext) {
    int cap = 0, sm = 0;
    for (int i = 0; ext[i]; i++) {
        if (isupper(ext[i])) cap++;
        else if (islower(ext[i])) sm++;
    }
    return cap - sm;
}

int main() {
    int param_count;
    scanf("%d", &param_count);
    
    char class_name[100];
    scanf("%s", class_name);
    
    int n;
    scanf("%d", &n);
    
    char **extensions = malloc(n * sizeof(char *));
    for (int i = 0; i < n; i++) {
        extensions[i] = malloc(100 * sizeof(char));
        scanf("%s", extensions[i]);
    }
    
    int max_strength = strength(extensions[0]);
    int max_idx = 0;
    
    for (int i = 1; i < n; i++) {
        int s = strength(extensions[i]);
        if (s > max_strength) {
            max_strength = s;
            max_idx = i;
        }
    }
    
    printf("%s.%s\n", class_name, extensions[max_idx]);
    
    for (int i = 0; i < n; i++) {
        free(extensions[i]);
    }
    free(extensions);
    
    return 0;
}
