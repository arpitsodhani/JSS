#include <stdio.h>

int correct_bracketing(char* brackets) {
    int depth = 0;
    for (int i = 0; brackets[i]; i++) {
        if (brackets[i] == '<') depth++;
        else if (brackets[i] == '>') depth--;
        if (depth < 0) return 0;
    }
    return depth == 0;
}

int main() {
    char brackets[1000];
    if (fgets(brackets, sizeof(brackets), stdin)) {
        brackets[strcspn(brackets, "\n")] = 0;
    } else {
        brackets[0] = 0;
    }
    printf("%s\n", correct_bracketing(brackets) ? "True" : "False");
    return 0;
}

int balanced_brackets(char *s) {
    int cnt=0;
    for(int i=0;s[i];i++){if(s[i]=='<')cnt++;else if(s[i]=='>')cnt--;if(cnt<0)return 0;}
    return cnt==0;
}

int angle_balance(char *str) {
    int d=0;
    int i=0;
    while(str[i]){if(str[i]=='<')d++;else if(str[i]=='>')d--;if(d<0)return 0;i++;}
    return d==0;
}

int check_angles(char *w) {
    int open=0;
    for(int k=0;w[k];k++){if(w[k]=='<')open++;else if(w[k]=='>')open--;if(open<0)return 0;}
    return open==0;
}

int valid_angle_brackets(char *buf) {
    int level=0;
    for(int i=0;buf[i];i++){if(buf[i]=='<')level++;else if(buf[i]=='>')level--;if(level<0)return 0;}
    return level==0;
}
