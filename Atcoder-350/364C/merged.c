#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void sort_dishes_by_sweetness_descending(int n, long long *sweetness, long long *saltiness) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (sweetness[j] > sweetness[i]) {
                long long tmp = sweetness[i];
                sweetness[i] = sweetness[j];
                sweetness[j] = tmp;
                tmp = saltiness[i];
                saltiness[i] = saltiness[j];
                saltiness[j] = tmp;
            }
        }
    }
}

int accumulate_until_sweetness_threshold(int n, long long *sweetness, long long threshold) {
    long long sum = 0;
    for (int i = 0; i < n; i++) {
        sum += sweetness[i];
        if (sum > threshold) {
            return i + 1;
        }
    }
    return n;
}

void sort_dishes_by_saltiness_descending(int n, long long *sweetness, long long *saltiness) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (saltiness[j] > saltiness[i]) {
                long long tmp = sweetness[i];
                sweetness[i] = sweetness[j];
                sweetness[j] = tmp;
                tmp = saltiness[i];
                saltiness[i] = saltiness[j];
                saltiness[j] = tmp;
            }
        }
    }
}

int accumulate_until_saltiness_threshold(int n, long long *saltiness, long long threshold) {
    long long sum = 0;
    for (int i = 0; i < n; i++) {
        sum += saltiness[i];
        if (sum > threshold) {
            return i + 1;
        }
    }
    return n;
}

int select_minimum_count(int sweet_count, int salty_count) {
    return sweet_count < salty_count ? sweet_count : salty_count;
}

int main() {
    int n;
    long long x, y, sweetness[200005], saltiness[200005];
    scanf("%d %lld %lld", &n, &x, &y);
    for (int i = 0; i < n; i++) scanf("%lld", &sweetness[i]);
    for (int i = 0; i < n; i++) scanf("%lld", &saltiness[i]);
    
    long long sweet_copy[200005], salty_copy[200005];
    for (int i = 0; i < n; i++) {
        sweet_copy[i] = sweetness[i];
        salty_copy[i] = saltiness[i];
    }
    
    sort_dishes_by_sweetness_descending(n, sweetness, saltiness);
    int sweet_count = accumulate_until_sweetness_threshold(n, sweetness, x);
    
    sort_dishes_by_saltiness_descending(n, sweet_copy, salty_copy);
    int salty_count = accumulate_until_saltiness_threshold(n, salty_copy, y);
    
    printf("%d\n", select_minimum_count(sweet_count, salty_count));
    return 0;
}