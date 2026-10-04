#include <stdio.h>

void incr_list(int* arr, int n, int* result) {
    for (int i = 0; i < n; i++) {
        result[i] = arr[i] + 1;
    }
}

int main() {
    int n;
    scanf("%d", &n);
    if (n == 0) {
        printf("\n");
        return 0;
    }
    int arr[n], result[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    incr_list(arr, n, result);
    for (int i = 0; i < n; i++) {
        if (i > 0) printf(" ");
        printf("%d", result[i]);
    }
    printf("\n");
    return 0;
}

void add_one(int *arr, int n) {
    for(int i=0;i<n;i++){if(i)printf(" ");printf("%d",arr[i]+1);}
    printf("\n");
}

void increment_vals(int *v, int sz) {
    int i=0;
    while(i<sz){if(i)printf(" ");printf("%d",v[i]+1);i++;}
    printf("\n");
}

void bump_up(int *nums, int cnt) {
    for(int k=0;k<cnt;k++){printf("%d",nums[k]+1);if(k<cnt-1)printf(" ");}
    printf("\n");
}

void plus_one(int *data, int len) {
    for(int i=0;i<len;i++){if(i)printf(" ");printf("%d",data[i]+1);}
    printf("\n");
}
