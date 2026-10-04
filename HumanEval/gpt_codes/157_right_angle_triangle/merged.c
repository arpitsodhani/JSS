#include <stdio.h>
#include <stdbool.h>

int main() {
    int param_count;
    scanf("%d", &param_count);
    
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    
    if (a*a + b*b == c*c || a*a + c*c == b*b || b*b + c*c == a*a) {
        printf("true\n");
    } else {
        printf("false\n");
    }
    
    return 0;
}
