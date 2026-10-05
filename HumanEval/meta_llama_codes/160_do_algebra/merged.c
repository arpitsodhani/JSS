#include <stdio.h>

int evaluate(int* operand, char* operators, int n) {
    
    for (int i = 0; i < n - 1; i++) {
        if (operators[i] == '*') {
            operand[i + 1] = operand[i] * operand[i + 1];
            operand[i] = 0;
            operators[i] = '+';
        } else if (operators[i] == '/') {
            operand[i + 1] = operand[i] / operand[i + 1];
            operand[i] = 0;
            operators[i] = '+';
        }
    }
    
    
    int result = operand[0];
    for (int i = 0; i < n - 1; i++) {
        if (operators[i] == '+') {
            result += operand[i + 1];
        } else if (operators[i] == '-') {
            result -= operand[i + 1];
        }
    }
    
    return result;
}

int main() {
    int n;
    scanf("%d", &n);
    
    int operand[100];
    char operators[100];
    
    for (int i = 0; i < n; i++) {
        scanf("%d", &operand[i]);
    }
    
    for (int i = 0; i < n - 1; i++) {
        scanf(" %c", &operators[i]);
    }
    
    printf("%d\n", evaluate(operand, operators, n));
    return 0;
}
