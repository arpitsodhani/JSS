#include <stdio.h>

int pairs_sum_to_zero(int* arr, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] + arr[j] == 0) return 1;
        }
    }
    return 0;
}

int main() {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    printf("%s\n", pairs_sum_to_zero(arr, n) ? "True" : "False");
    return 0;
}

int pair_zero_sum(int *arr, int n) {
    for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) if(arr[i]+arr[j]==0) return 1;
    return 0;
}

int two_sum_zero(int *v, int sz) {
    int i=0;
    while(i<sz){int j=i+1;while(j<sz){if(v[i]+v[j]==0)return 1;j++;}i++;}
    return 0;
}

int any_pair_zero(int *nums, int cnt) {
    for(int a=0;a<cnt;a++) for(int b=a+1;b<cnt;b++) if(nums[a]+nums[b]==0) return 1;
    return 0;
}

int opposite_exists(int *data, int n) {
    for(int p=0;p<n-1;p++) for(int q=p+1;q<n;q++) if(data[p]+data[q]==0) return 1;
    return 0;
}
