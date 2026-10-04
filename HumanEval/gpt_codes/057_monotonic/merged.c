#include <stdio.h>

int monotonic(int* arr, int n) {
    if (n <= 1) return 1;
    int increasing = 1, decreasing = 1;
    for (int i = 1; i < n; i++) {
        if (arr[i] > arr[i-1]) decreasing = 0;
        if (arr[i] < arr[i-1]) increasing = 0;
    }
    return increasing || decreasing;
}

int main() {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    printf("%s\n", monotonic(arr, n) ? "True" : "False");
    return 0;
}

int is_monotone(int *arr, int n) {
    if(n<=1) return 1;
    int inc=1,dec=1;
    for(int i=1;i<n;i++){if(arr[i]>arr[i-1])dec=0;if(arr[i]<arr[i-1])inc=0;}
    return inc||dec;
}

int monotone_check(int *v, int sz) {
    int up=1,dn=1;
    int i=1;
    while(i<sz){if(v[i]<v[i-1])up=0;if(v[i]>v[i-1])dn=0;i++;}
    return up||dn;
}

int non_decreasing_or_increasing(int *a, int n) {
    int asc=1,desc=1;
    for(int k=1;k<n;k++){if(a[k]<a[k-1])asc=0;if(a[k]>a[k-1])desc=0;}
    return asc||desc;
}

int sorted_order(int *nums, int cnt) {
    if(cnt<=1) return 1;
    int gt=1,lt=1;
    for(int i=1;i<cnt;i++){if(nums[i]>nums[i-1])lt=0;if(nums[i]<nums[i-1])gt=0;}
    return gt||lt;
}
