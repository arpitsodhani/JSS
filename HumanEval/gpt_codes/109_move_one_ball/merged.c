#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int move_one_ball(int n, int arr[]) {
    if (n == 0) return 1;
    
    int rotations = 0;
    for (int i = 0; i < n; i++) {
        int sorted = 1;
        for (int j = 0; j < n - 1; j++) {
            if (arr[(i + j) % n] > arr[(i + j + 1) % n]) {
                sorted = 0;
                break;
            }
        }
        if (sorted) return 1;
    }
    return 0;
}

void run(void) {

    int n;
    scanf("%d", &n);
    if (n == 0) {
        printf("True\n");
        return 0;
    }
    int arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    printf("%s\n", move_one_ball(n, arr) ? "True" : "False");
}

int main() {
    run();
    return 0;
}
