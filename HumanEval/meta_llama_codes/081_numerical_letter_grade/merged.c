#include <stdio.h>

void numerical_grade(double *grades, int n, char result[][10]) {
    for (int i = 0; i < n; i++) {
        if (grades[i] >= 3.9999) strcpy(result[i], "A+");
        else if (grades[i] >= 3.7) strcpy(result[i], "A");
        else if (grades[i] >= 3.3) strcpy(result[i], "A-");
        else if (grades[i] >= 3.0) strcpy(result[i], "B+");
        else if (grades[i] >= 2.7) strcpy(result[i], "B");
        else if (grades[i] >= 2.3) strcpy(result[i], "B-");
        else if (grades[i] >= 2.0) strcpy(result[i], "C+");
        else if (grades[i] >= 1.7) strcpy(result[i], "C");
        else if (grades[i] >= 1.3) strcpy(result[i], "C-");
        else if (grades[i] >= 1.0) strcpy(result[i], "D+");
        else if (grades[i] >= 0.7) strcpy(result[i], "D");
        else if (grades[i] >= 0.0) strcpy(result[i], "D-");
        else strcpy(result[i], "E");
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    double grades[n];
    for (int i = 0; i < n; i++) scanf("%lf", &grades[i]);
    char result[n][10];
    numerical_grade(grades, n, result);
    for (int i = 0; i < n; i++) {
        printf("%s", result[i]);
        if (i < n - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
