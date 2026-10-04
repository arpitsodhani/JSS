#include <stdio.h>

int car_race_collision(int n) {
    return n * n;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", car_race_collision(n));
    return 0;
}

int collision_count(int n) {
    return n * n;
}

int total_collisions(int cars) {
    return cars * cars;
}

int race_result(int num) {
    int res = num;
    res *= num;
    return res;
}

int compute_collisions(int k) {
    return k * k;
}
