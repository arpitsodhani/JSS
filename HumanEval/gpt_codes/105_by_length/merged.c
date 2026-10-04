#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char* number_to_word(int n) {
    switch(n) {
        case 1: return "One";
        case 2: return "Two";
        case 3: return "Three";
        case 4: return "Four";
        case 5: return "Five";
        case 6: return "Six";
        case 7: return "Seven";
        case 8: return "Eight";
        case 9: return "Nine";
        default: return NULL;
    }
}

int compare_desc(const void *a, const void *b) {
    return *(int*)b - *(int*)a;
}

void by_length(int n, int arr[], char result[][20], int *result_size) {
    int valid[n];
    int valid_count = 0;
    
    for (int i = 0; i < n; i++) {
        if (arr[i] >= 1 && arr[i] <= 9) {
            valid[valid_count++] = arr[i];
        }
    }
    
    qsort(valid, valid_count, sizeof(int), compare_desc);
    
    *result_size = 0;
    for (int i = 0; i < valid_count; i++) {
        const char *word = number_to_word(valid[i]);
        if (word) {
            strcpy(result[(*result_size)++], word);
        }
    }
}

void run(void) {

    int n;
    scanf("%d", &n);
    if (n == 0) {
        printf("\n");
        return 0;
    }
    int arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    char result[n][20];
    int result_size;
    by_length(n, arr, result, &result_size);
    for (int i = 0; i < result_size; i++) {
        printf("%s", result[i]);
        if (i < result_size - 1) printf(" ");
    }
    printf("\n");
}

int main() {
    run();
    return 0;
}
