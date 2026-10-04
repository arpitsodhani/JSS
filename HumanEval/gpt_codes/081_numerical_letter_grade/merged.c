#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

const char* get_letter_grade(double gpa) {
    if (gpa == 4.0) return "A+";
    if (gpa > 3.7) return "A";
    if (gpa > 3.3) return "A-";
    if (gpa > 3.0) return "B+";
    if (gpa > 2.7) return "B";
    if (gpa > 2.3) return "B-";
    if (gpa > 2.0) return "C+";
    if (gpa > 1.7) return "C";
    if (gpa > 1.3) return "C-";
    if (gpa > 1.0) return "D+";
    if (gpa > 0.7) return "D";
    if (gpa > 0.0) return "D-";
    return "E";
}

void numerical_letter_grade(int n, double grades[]) {
    for (int i = 0; i < n; i++) {
        printf("%s", get_letter_grade(grades[i]));
        if (i < n - 1) printf(" ");
    }
    printf("\n");
}

int main() {
    int n;
    scanf("%d", &n);
    if (n == 0) {
        printf("\n");
        return 0;
    }
    double grades[n];
    for (int i = 0; i < n; i++) {
        scanf("%lf", &grades[i]);
    }
    numerical_letter_grade(n, grades);
    return 0;
}

