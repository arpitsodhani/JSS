#include <stdio.h>

double parse_number(char* s) {
    double result = 0.0;
    double decimal = 0.0;
    int decimal_places = 0;
    int in_decimal = 0;
    
    for (int i = 0; s[i] != '\0' && s[i] != '\n'; i++) {
        if (s[i] == '.' || s[i] == ',') {
            in_decimal = 1;
        } else if (s[i] >= '0' && s[i] <= '9') {
            if (in_decimal) {
                decimal = decimal * 10 + (s[i] - '0');
                decimal_places++;
            } else {
                result = result * 10 + (s[i] - '0');
            }
        }
    }
    
    while (decimal_places > 0) {
        decimal /= 10.0;
        decimal_places--;
    }
    
    return result + decimal;
}

int main() {
    char a[100], b[100];
    scanf("%s %s", a, b);
    
    double val_a = parse_number(a);
    double val_b = parse_number(b);
    
    if (val_a > val_b) {
        printf("%s\n", a);
    } else if (val_b > val_a) {
        printf("%s\n", b);
    } else {
        printf("None\n");
    }
    
    return 0;
}
