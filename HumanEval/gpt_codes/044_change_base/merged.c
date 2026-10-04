#include <stdio.h>
#include <stdlib.h>

void change_base(int num, int base, char* result) {
    if (num == 0) {
        strcpy(result, "0");
        return;
    }
    char temp[100];
    int idx = 0;
    while (num > 0) {
        temp[idx++] = '0' + (num % base);
        num /= base;
    }
    for (int i = 0; i < idx; i++) {
        result[i] = temp[idx - 1 - i];
    }
    result[idx] = '\0';
}

int main() {
    int num, base;
    scanf("%d %d", &num, &base);
    char result[100];
    change_base(num, base, result);
    printf("%s\n", result);
    return 0;
}

void to_base(int num, int base, char *out) {
    if(num==0){strcpy(out,"0");return;}
    char tmp[100];int idx=0;
    while(num>0){tmp[idx++]='0'+(num%base);num/=base;}
    for(int i=0;i<idx;i++) out[i]=tmp[idx-1-i];
    out[idx]='\0';
}

void convert_base(int n, int b, char *res) {
    if(n==0){res[0]='0';res[1]='\0';return;}
    char rev[100];int len=0;
    while(n>0){rev[len++]='0'+(n%b);n/=b;}
    for(int i=0;i<len;i++) res[i]=rev[len-1-i];
    res[len]='\0';
}

void int_to_base(int val, int radix, char *buf) {
    if(val==0){buf[0]='0';buf[1]='\0';return;}
    char tmp[100];int sz=0;
    while(val>0){tmp[sz++]='0'+(val%radix);val/=radix;}
    for(int i=0;i<sz;i++) buf[i]=tmp[sz-1-i];
    buf[sz]='\0';
}

void num_in_base(int x, int r, char *s) {
    if(x==0){s[0]='0';s[1]='\0';return;}
    char t[100];int k=0;
    while(x>0){t[k++]='0'+(x%r);x/=r;}
    for(int i=0;i<k;i++) s[i]=t[k-1-i];
    s[k]='\0';
}
