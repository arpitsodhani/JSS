#include <stdio.h>
int main() {
    int n, arr[1000], count=0, sum=0;
    scanf("%d", &n);
    
    while(scanf("%d", &arr[count]) == 1) {
        count++;
    }
    
    for(int i=0; i<count; i++) {
        if(i%3==0) sum += arr[i]*arr[i];
        else if(i%4==0) sum += arr[i]*arr[i]*arr[i];
        else sum += arr[i];
    }
    
    printf("%d\n", sum);
    return 0;
}
