#include <stdio.h>

int triples_sum_to_zero(int* arr, int n) {
    for (int i = 0; i < n - 2; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            for (int k = j + 1; k < n; k++) {
                if (arr[i] + arr[j] + arr[k] == 0) return 1;
            }
        }
    }
    return 0;
}

int main() {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    printf("%s\n", triples_sum_to_zero(arr, n) ? "True" : "False");
    return 0;
}

int three_sum_zero(int *arr, int n) {
    for(int i=0;i<n-2;i++) for(int j=i+1;j<n-1;j++) for(int k=j+1;k<n;k++) if(arr[i]+arr[j]+arr[k]==0) return 1;
    return 0;
}

int triplet_sums_zero(int *v, int n) {
    int i=0;
    while(i<n-2){int j=i+1;while(j<n-1){int k=j+1;while(k<n){if(v[i]+v[j]+v[k]==0)return 1;k++;}j++;}i++;}
    return 0;
}

int any_triple_zero(int *a, int n) {
    for(int p=0;p<n;p++) for(int q=p+1;q<n;q++) for(int r=q+1;r<n;r++) if(a[p]+a[q]+a[r]==0) return 1;
    return 0;
}

int check_triple_sum(int *nums, int cnt) {
    for(int x=0;x<cnt-2;x++) for(int y=x+1;y<cnt-1;y++) for(int z=y+1;z<cnt;z++) if(nums[x]+nums[y]+nums[z]==0) return 1;
    return 0;
}
