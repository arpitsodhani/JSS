#include <stdio.h>

void sort_even(int *arr, int n) {
    for (int i = 0; i < n; i += 2) {
        for (int j = i+2; j < n; j += 2) {
            if (arr[i] > arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        printf("%d", arr[i]);
        if (i < n-1) printf(" ");
    }
    printf("\n");
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    sort_even(arr, n);
    return 0;
}

void sort_evens(int *nums, int size) {
    for (int i = 0; i < size; i += 2) {
        for (int j = i+2; j < size; j += 2) {
            if (nums[i] > nums[j]) {
                int tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
            }
        }
    }
    for (int i = 0; i < size; i++) {
        printf("%d", nums[i]);
        if (i < size-1) printf(" ");
    }
    printf("\n");
}

void sort_even_indices(int *arr, int n) {
    for(int i=0;i<n;i+=2) for(int j=i+2;j<n;j+=2) if(arr[i]>arr[j]){int t=arr[i];arr[i]=arr[j];arr[j]=t;}
    for(int i=0;i<n;i++){printf("%d",arr[i]);if(i<n-1)printf(" ");}
    printf("\n");
}

void order_even_pos(int *v, int sz) {
    for(int i=0;i<sz;i+=2) for(int j=i+2;j<sz;j+=2) if(v[i]>v[j]){int t=v[i];v[i]=v[j];v[j]=t;}
    for(int i=0;i<sz;i++){if(i)printf(" ");printf("%d",v[i]);}
    printf("\n");
}

void sort_even_slots(int *nums, int cnt) {
    for(int a=0;a<cnt;a+=2) for(int b=a+2;b<cnt;b+=2) if(nums[a]>nums[b]){int tmp=nums[a];nums[a]=nums[b];nums[b]=tmp;}
    for(int i=0;i<cnt;i++){printf("%d",nums[i]);if(i<cnt-1)printf(" ");}
    printf("\n");
}
