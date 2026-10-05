#include <stdio.h>

int main() {
    int param_count;
    scanf("%d", &param_count);
    
    int number, need, remaining;
    scanf("%d %d %d", &number, &need, &remaining);
    
    int can_eat = (remaining >= need) ? need : remaining;
    int total_eaten = number + can_eat;
    int left = remaining - can_eat;
    
    printf("[%d, %d]\n", total_eaten, left);
    return 0;
}
