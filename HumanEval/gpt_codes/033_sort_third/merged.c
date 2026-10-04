#include <stdio.h>

void sort_third(int *arr, int n) {
    for (int i = 0; i < n; i += 3) {
        for (int j = i+3; j < n; j += 3) {
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
    sort_third(arr, n);
    return 0;
}

void sort_every_third(int *data, int size) {
    for (int i = 0; i < size; i += 3) {
        for (int j = i+3; j < size; j += 3) {
            if (data[i] > data[j]) {
                int tmp = data[i];
                data[i] = data[j];
                data[j] = tmp;
            }
        }
    }
    for (int i = 0; i < size; i++) {
        printf("%d", data[i]);
        if (i < size-1) printf(" ");
    }
    printf("\n");
}

void order_thirds(int *arr, int n) {
    for(int i=0;i<n;i+=3) for(int j=i+3;j<n;j+=3) if(arr[i]>arr[j]){int t=arr[i];arr[i]=arr[j];arr[j]=t;}
    for(int i=0;i<n;i++){printf("%d",arr[i]);if(i<n-1)printf(" ");}
    printf("\n");
}

void sort_step3(int *nums, int cnt) {
    for(int i=0;i<cnt;i+=3) for(int j=i+3;j<cnt;j+=3) if(nums[i]>nums[j]){int tmp=nums[i];nums[i]=nums[j];nums[j]=tmp;}
    for(int i=0;i<cnt;i++){if(i)printf(" ");printf("%d",nums[i]);}
    printf("\n");
}

void sort_multiples_of_3(int *data, int sz) {
    for(int a=0;a<sz;a+=3) for(int b=a+3;b<sz;b+=3) if(data[a]>data[b]){int t=data[a];data[a]=data[b];data[b]=t;}
    for(int i=0;i<sz;i++){printf("%d",data[i]);if(i<sz-1)printf(" ");}
    printf("\n");
}
