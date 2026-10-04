#include <stdio.h>
#include <string.h>

int is_palindrome(char* str) {
    int len = strlen(str);
    for (int i = 0; i < len / 2; i++) {
        if (str[i] != str[len - 1 - i]) return 0;
    }
    return 1;
}

int main() {
    char str[1000];
    if (fgets(str, sizeof(str), stdin)) {
        str[strcspn(str, "\n")] = 0;
    } else {
        str[0] = 0;
    }
    printf("%s\n", is_palindrome(str) ? "True" : "False");
    return 0;
}

int check_palindrome(char *s) {
    int n=strlen(s);
    for(int i=0;i<n/2;i++) if(s[i]!=s[n-1-i]) return 0;
    return 1;
}

int pal_test(char *str) {
    int len=strlen(str),lo=0,hi=len-1;
    while(lo<hi){if(str[lo]!=str[hi])return 0;lo++;hi--;}
    return 1;
}

int palindrome_check(char *w) {
    int n=strlen(w);
    int i=0;
    while(i<n/2){if(w[i]!=w[n-1-i])return 0;i++;}
    return 1;
}

int is_mirror(char *buf) {
    int n=strlen(buf);
    for(int k=0;k<n/2;k++) if(buf[k]!=buf[n-1-k]) return 0;
    return 1;
}
