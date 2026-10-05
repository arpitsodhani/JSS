#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void *a, const void *b) {
    char **str_a = (char **)a;
    char **str_b = (char **)b;
    int len_a = strlen(*str_a);
    int len_b = strlen(*str_b);
    
    if (len_a != len_b) return len_a - len_b;
    return strcmp(*str_a, *str_b);
}

int main() {
    int param_count;
    scanf("%d", &param_count);
    
    int n;
    scanf("%d", &n);
    
    char **lst = malloc(n * sizeof(char *));
    for (int i = 0; i < n; i++) {
        lst[i] = malloc(100 * sizeof(char));
        scanf("%s", lst[i]);
    }
    
    char **filtered = malloc(n * sizeof(char *));
    int count = 0;
    
    for (int i = 0; i < n; i++) {
        if (strlen(lst[i]) % 2 == 0) {
            filtered[count++] = lst[i];
        }
    }
    
    qsort(filtered, count, sizeof(char *), compare);
    
    printf("[");
    for (int i = 0; i < count; i++) {
        if (i > 0) printf(", ");
        printf("\"%s\"", filtered[i]);
    }
    printf("]\n");
    
    for (int i = 0; i < n; i++) {
        free(lst[i]);
    }
    free(lst);
    free(filtered);
    
    return 0;
}
