#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

const char* exchange(int n1, int lst1[], int n2, int lst2[]) {
    int odd_count_lst1 = 0;
    int even_count_lst2 = 0;
    
    for (int i = 0; i < n1; i++) {
        if (lst1[i] % 2 == 1) odd_count_lst1++;
    }
    
    for (int i = 0; i < n2; i++) {
        if (lst2[i] % 2 == 0) even_count_lst2++;
    }
    
    return (even_count_lst2 >= odd_count_lst1) ? "YES" : "NO";
}

int main() {
    int n1, n2;
    scanf("%d", &n1);
    int lst1[n1];
    for (int i = 0; i < n1; i++) {
        scanf("%d", &lst1[i]);
    }
    scanf("%d", &n2);
    int lst2[n2];
    for (int i = 0; i < n2; i++) {
        scanf("%d", &lst2[i]);
    }
    printf("%s\n", exchange(n1, lst1, n2, lst2));
    return 0;
}

