#include <stdio.h>

int below_threshold(int* arr, int n, int threshold) {
    for (int i = 0; i < n; i++) {
        if (arr[i] >= threshold) return 0;
    }
    return 1;
}

int main() {
    int n, threshold;
    scanf("%d %d", &n, &threshold);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    printf("%s\n", below_threshold(arr, n, threshold) ? "True" : "False");
    return 0;
}

int all_below(int *arr, int n, int t) {
    for(int i=0;i<n;i++) if(arr[i]>=t) return 0;
    return 1;
}

int under_limit(int *v, int sz, int limit) {
    int i=0;
    while(i<sz){if(v[i]>=limit)return 0;i++;}
    return 1;
}

int check_threshold(int *nums, int cnt, int thr) {
    for(int k=0;k<cnt;k++) if(nums[k]>=thr) return 0;
    return 1;
}

int less_than_max(int *data, int len, int max) {
    for(int i=0;i<len;i++) if(data[i]>=max) return 0;
    return 1;
}
