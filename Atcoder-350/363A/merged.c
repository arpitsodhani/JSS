#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_rating(int *r) {
    scanf("%d", r);
}

int compute_needed_increase(int r) {
    int current_tier = (r - 1) / 100;
    int next_tier_start = (current_tier + 1) * 100;
    return next_tier_start - r;
}

int main() {
    int r;
    read_rating(&r);
    printf("%d\n", compute_needed_increase(r));
    return 0;
}
