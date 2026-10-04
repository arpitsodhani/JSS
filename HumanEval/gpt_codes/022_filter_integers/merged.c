#include <stdio.h>

void filter_ints(char strs[][100], int n) {
    int first = 1;
    for (int i = 0; i < n; i++) {
        int is_int = 1;
        for (int j = 0; strs[i][j]; j++) {
            if ((strs[i][j] < '0' || strs[i][j] > '9') && strs[i][j] != '-') {
                is_int = 0;
                break;
            }
        }
        if (is_int && strs[i][0]) {
            if (!first) printf(" ");
            printf("%s", strs[i]);
            first = 0;
        }
    }
    printf("\n");
}

int main(void) {
    int n;
    scanf("%d", &n);
    char strs[n][100];
    for (int i = 0; i < n; i++) scanf("%s", strs[i]);
    filter_ints(strs, n);
    return 0;
}

void get_integers(char items[][100], int count) {
    int found = 0;
    for (int i = 0; i < count; i++) {
        int valid = 1;
        for (int j = 0; items[i][j]; j++) {
            if ((items[i][j] < '0' || items[i][j] > '9') && items[i][j] != '-') {
                valid = 0;
                break;
            }
        }
        if (valid && items[i][0]) {
            if (found > 0) printf(" ");
            printf("%s", items[i]);
            found++;
        }
    }
    printf("\n");
}

void keep_integers(char strs[][100], int n) {
    int first=1;
    for (int i=0;i<n;i++) {
        int ok=1;
        for (int j=0;strs[i][j];j++) if((strs[i][j]<'0'||strs[i][j]>'9')&&strs[i][j]!='-'){ok=0;break;}
        if(ok&&strs[i][0]){if(!first)printf(" ");printf("%s",strs[i]);first=0;}
    }
    printf("\n");
}

void select_ints(char items[][100], int cnt) {
    int found=0;
    for (int i=0;i<cnt;i++) {
        int valid=1;
        for (int j=0;items[i][j];j++) if((items[i][j]<'0'||items[i][j]>'9')&&items[i][j]!='-'){valid=0;break;}
        if(valid&&items[i][0]){if(found>0)printf(" ");printf("%s",items[i]);found++;}
    }
    printf("\n");
}

void extract_ints(char ws[][100], int sz) {
    int cnt=0;
    for (int i=0;i<sz;i++) {
        int is_int=1;
        for (int j=0;ws[i][j];j++) if((ws[i][j]<'0'||ws[i][j]>'9')&&ws[i][j]!='-'){is_int=0;break;}
        if(is_int&&ws[i][0]){if(cnt>0)printf(" ");printf("%s",ws[i]);cnt++;}
    }
    printf("\n");
}
