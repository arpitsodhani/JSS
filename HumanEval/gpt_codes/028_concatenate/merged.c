#include <stdio.h>

void concat(char strs[][100], int n) {
    for (int i = 0; i < n; i++) {
        printf("%s", strs[i]);
    }
    printf("\n");
}

void run(void) {

    int n;
    scanf("%d", &n);
    char strs[n][100];
    for (int i = 0; i < n; i++) scanf("%s", strs[i]);
    concat(strs, n);
}

int main() {
    run();
    return 0;
}

void join_strings(char strings[][100], int count) {
    for (int i = 0; i < count; i++) {
        printf("%s", strings[i]);
    }
    printf("\n");
}

void join_all(char strs[][100], int n) {
    for(int i=0;i<n;i++) printf("%s",strs[i]);
    printf("\n");
}

void append_all(char words[][100], int cnt) {
    int i=0;
    while(i<cnt){printf("%s",words[i]);i++;}
    printf("\n");
}

void merge_strings(char ws[][100], int sz) {
    for(int k=0;k<sz;k++) printf("%s",ws[k]);
    printf("\n");
}
