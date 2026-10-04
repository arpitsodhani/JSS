#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_sorted(int n, int arr[]) {
    if (n <= 1) return 1;
    
    int count[10001] = {0};
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
        if (count[arr[i]] > 2) return 0;
    }
    
    for (int i = 1; i < n; i++) {
        if (arr[i] < arr[i-1]) return 0;
    }
    
    return 1;
}

void run(void) {

    int test_cases;
    scanf("%d", &test_cases);
    
    char line[10000];
    int has_data = scanf(" %[^\n]", line);
    
    if (has_data != 1) {
        printf("True\n");
        return 0;
    }
    
    int arr[1000], arr_size = 0;
    char *token = strtok(line, " ");
    while (token != NULL) {
        arr[arr_size++] = atoi(token);
        token = strtok(NULL, " ");
    }
    
    if (is_sorted(arr_size, arr)) {
        printf("True\n");
    } else {
        printf("False\n");
    }
}

int main() {
    run();
    return 0;
}

int is_sorted(int n, int arr[]) {
    if (n <= 1) return 1;
    
    int count[10001] = {0};
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
        if (count[arr[i]] > 2) return 0;
    }
    
    for (int i = 1; i < n; i++) {
        if (arr[i] < arr[i-1]) return 0;
    }
    
    return 1;
}

int is_sorted(int n, int arr[]) {
    if (n <= 1) return 1;
    
    int count[10001] = {0};
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
        if (count[arr[i]] > 2) return 0;
    }
    
    for (int i = 1; i < n; i++) {
        if (arr[i] < arr[i-1]) return 0;
    }
    
    return 1;
}

int is_sorted(int n, int arr[]) {
    if (n <= 1) return 1;
    
    int count[10001] = {0};
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
        if (count[arr[i]] > 2) return 0;
    }
    
    for (int i = 1; i < n; i++) {
        if (arr[i] < arr[i-1]) return 0;
    }
    
    return 1;
}

int is_sorted(int n, int arr[]) {
    if (n <= 1) return 1;
    
    int count[10001] = {0};
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
        if (count[arr[i]] > 2) return 0;
    }
    
    for (int i = 1; i < n; i++) {
        if (arr[i] < arr[i-1]) return 0;
    }
    
    return 1;
}
