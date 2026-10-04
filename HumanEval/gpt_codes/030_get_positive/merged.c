#include <stdio.h>

void get_positive(int *arr, int n) {
    int first = 1;
    for (int i = 0; i < n; i++) {
        if (arr[i] > 0) {
            if (!first) printf(" ");
            printf("%d", arr[i]);
            first = 0;
        }
    }
    printf("\n");
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    get_positive(arr, n);
    return 0;
}

void filter_positive(int *nums, int size) {
    int found = 0;
    for (int i = 0; i < size; i++) {
        if (nums[i] > 0) {
            if (found > 0) printf(" ");
            printf("%d", nums[i]);
            found++;
        }
    }
    printf("\n");
}

void positive_vals(int *arr, int n) {
    int first=1;
    for(int i=0;i<n;i++)if(arr[i]>0){if(!first)printf(" ");printf("%d",arr[i]);first=0;}
    printf("\n");
}

void select_positive(int *v, int sz) {
    int cnt=0;
    for(int i=0;i<sz;i++)if(v[i]>0){if(cnt)printf(" ");printf("%d",v[i]);cnt++;}
    printf("\n");
}

void above_zero(int *nums, int len) {
    int p=0;
    for(int k=0;k<len;k++)if(nums[k]>0){if(p)printf(" ");printf("%d",nums[k]);p++;}
    printf("\n");
}
