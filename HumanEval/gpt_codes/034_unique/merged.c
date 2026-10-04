#include <stdio.h>

void unique_sorted(int *arr, int n) {
    int result[1000], count = 0;
    for (int i = 0; i < n; i++) {
        int found = 0;
        for (int j = 0; j < count; j++) {
            if (result[j] == arr[i]) {
                found = 1;
                break;
            }
        }
        if (!found) result[count++] = arr[i];
    }
    for (int i = 0; i < count-1; i++) {
        for (int j = i+1; j < count; j++) {
            if (result[i] > result[j]) {
                int temp = result[i];
                result[i] = result[j];
                result[j] = temp;
            }
        }
    }
    for (int i = 0; i < count; i++) {
        printf("%d", result[i]);
        if (i < count-1) printf(" ");
    }
    printf("\n");
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    unique_sorted(arr, n);
    return 0;
}

void distinct_sorted(int *nums, int size) {
    int output[1000], num = 0;
    for (int i = 0; i < size; i++) {
        int exists = 0;
        for (int j = 0; j < num; j++) {
            if (output[j] == nums[i]) {
                exists = 1;
                break;
            }
        }
        if (!exists) output[num++] = nums[i];
    }
    for (int i = 0; i < num-1; i++) {
        for (int j = i+1; j < num; j++) {
            if (output[i] > output[j]) {
                int tmp = output[i];
                output[i] = output[j];
                output[j] = tmp;
            }
        }
    }
    for (int i = 0; i < num; i++) {
        printf("%d", output[i]);
        if (i < num-1) printf(" ");
    }
    printf("\n");
}

void sorted_unique(int *arr, int n) {
    int res[1000],cnt=0;
    for(int i=0;i<n;i++){int f=0;for(int j=0;j<cnt;j++)if(res[j]==arr[i]){f=1;break;}if(!f)res[cnt++]=arr[i];}
    for(int i=0;i<cnt-1;i++) for(int j=i+1;j<cnt;j++) if(res[i]>res[j]){int t=res[i];res[i]=res[j];res[j]=t;}
    for(int i=0;i<cnt;i++){printf("%d",res[i]);if(i<cnt-1)printf(" ");}
    printf("\n");
}

void dedup_sorted(int *vals, int sz) {
    int out[1000],n=0;
    for(int i=0;i<sz;i++){int dup=0;for(int k=0;k<n;k++)if(out[k]==vals[i]){dup=1;break;}if(!dup)out[n++]=vals[i];}
    for(int i=0;i<n-1;i++) for(int j=i+1;j<n;j++) if(out[i]>out[j]){int t=out[i];out[i]=out[j];out[j]=t;}
    for(int i=0;i<n;i++){if(i)printf(" ");printf("%d",out[i]);}
    printf("\n");
}

void unique_asc(int *data, int len) {
    int buf[1000],cnt=0;
    for(int i=0;i<len;i++){int found=0;for(int k=0;k<cnt;k++)if(buf[k]==data[i]){found=1;break;}if(!found)buf[cnt++]=data[i];}
    for(int i=0;i<cnt-1;i++) for(int j=i+1;j<cnt;j++) if(buf[i]>buf[j]){int tmp=buf[i];buf[i]=buf[j];buf[j]=tmp;}
    for(int i=0;i<cnt;i++){printf("%d",buf[i]);if(i<cnt-1)printf(" ");}
    printf("\n");
}
