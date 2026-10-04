#include <stdio.h>

int max_element(int *arr, int n) {
    int max_val = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max_val) max_val = arr[i];
    }
    return max_val;
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    printf("%d\n", max_element(arr, n));
    return 0;
}

int find_max(int *nums, int size) {
    int maximum = nums[0];
    for (int i = 1; i < size; i++) {
        if (nums[i] > maximum) maximum = nums[i];
    }
    return maximum;
}

int array_max(int *arr, int n) {
    int m=arr[0];
    for(int i=1;i<n;i++) if(arr[i]>m) m=arr[i];
    return m;
}

int get_max(int *v, int sz) {
    int best=v[0];
    int k=1;
    while(k<sz){if(v[k]>best)best=v[k];k++;}
    return best;
}

int peak_value(int *nums, int cnt) {
    int high=nums[0];
    for(int i=1;i<cnt;i++) if(nums[i]>high) high=nums[i];
    return high;
}
