#include <stdio.h>
#include <string.h>

int get_num_value(char *word) {
    if (strcmp(word, "zero") == 0) return 0;
    if (strcmp(word, "one") == 0) return 1;
    if (strcmp(word, "two") == 0) return 2;
    if (strcmp(word, "three") == 0) return 3;
    if (strcmp(word, "four") == 0) return 4;
    if (strcmp(word, "five") == 0) return 5;
    if (strcmp(word, "six") == 0) return 6;
    if (strcmp(word, "seven") == 0) return 7;
    if (strcmp(word, "eight") == 0) return 8;
    if (strcmp(word, "nine") == 0) return 9;
    return -1;
}

void sort_numbers(char *s) {
    char words[100][20];
    int count = 0;
    char *token = strtok(s, " ");
    while (token) {
        strcpy(words[count++], token);
        token = strtok(NULL, " ");
    }
    for (int i = 0; i < count-1; i++) {
        for (int j = i+1; j < count; j++) {
            if (get_num_value(words[i]) > get_num_value(words[j])) {
                char temp[20];
                strcpy(temp, words[i]);
                strcpy(words[i], words[j]);
                strcpy(words[j], temp);
            }
        }
    }
    for (int i = 0; i < count; i++) {
        printf("%s", words[i]);
        if (i < count-1) printf(" ");
    }
    printf("\n");
}

int main(void) {
    char s[1000];
    scanf("%[^\n]", s);
    sort_numbers(s);
    return 0;
}

int word_to_int(char *w) {
    if (strcmp(w, "zero") == 0) return 0;
    if (strcmp(w, "one") == 0) return 1;
    if (strcmp(w, "two") == 0) return 2;
    if (strcmp(w, "three") == 0) return 3;
    if (strcmp(w, "four") == 0) return 4;
    if (strcmp(w, "five") == 0) return 5;
    if (strcmp(w, "six") == 0) return 6;
    if (strcmp(w, "seven") == 0) return 7;
    if (strcmp(w, "eight") == 0) return 8;
    if (strcmp(w, "nine") == 0) return 9;
    return -1;
}

void sort_word_nums(char *input) {
    char items[100][20];
    int num = 0;
    char *tok = strtok(input, " ");
    while (tok) {
        strcpy(items[num++], tok);
        tok = strtok(NULL, " ");
    }
    for (int i = 0; i < num-1; i++) {
        for (int j = i+1; j < num; j++) {
            if (word_to_int(items[i]) > word_to_int(items[j])) {
                char tmp[20];
                strcpy(tmp, items[i]);
                strcpy(items[i], items[j]);
                strcpy(items[j], tmp);
            }
        }
    }
    for (int i = 0; i < num; i++) {
        printf("%s", items[i]);
        if (i < num-1) printf(" ");
    }
    printf("\n");
}

int name_to_val(char *w) {
    if (!strcmp(w,"zero")) return 0; if (!strcmp(w,"one")) return 1;
    if (!strcmp(w,"two")) return 2; if (!strcmp(w,"three")) return 3;
    if (!strcmp(w,"four")) return 4; if (!strcmp(w,"five")) return 5;
    if (!strcmp(w,"six")) return 6; if (!strcmp(w,"seven")) return 7;
    if (!strcmp(w,"eight")) return 8; if (!strcmp(w,"nine")) return 9;
    return -1;
}

void sort_num_words(char *s) {
    char ws[100][20]; int n=0;
    char *tok = strtok(s, " ");
    while (tok) { strcpy(ws[n++], tok); tok = strtok(NULL, " "); }
    for (int i=0;i<n-1;i++) for (int j=i+1;j<n;j++) if (name_to_val(ws[i])>name_to_val(ws[j])) { char t[20]; strcpy(t,ws[i]); strcpy(ws[i],ws[j]); strcpy(ws[j],t); }
    for (int i=0;i<n;i++) { printf("%s", ws[i]); if(i<n-1) printf(" "); }
    printf("\n");
}

int digit_name_order(char *w) {
    char *names[] = {"zero","one","two","three","four","five","six","seven","eight","nine"};
    for (int i=0;i<10;i++) if (!strcmp(w, names[i])) return i;
    return -1;
}

void arrange_number_names(char *input) {
    char words[100][20]; int cnt=0;
    char *t = strtok(input, " ");
    while (t) { strcpy(words[cnt++], t); t = strtok(NULL, " "); }
    for (int i=0;i<cnt-1;i++) for (int j=i+1;j<cnt;j++) if (digit_name_order(words[i])>digit_name_order(words[j])) { char buf[20]; strcpy(buf,words[i]); strcpy(words[i],words[j]); strcpy(words[j],buf); }
    for (int i=0;i<cnt;i++) { printf("%s", words[i]); if(i<cnt-1) printf(" "); }
    printf("\n");
}

int numword_rank(char *w) {
    if (!strcmp(w,"zero")) return 0; if (!strcmp(w,"one")) return 1;
    if (!strcmp(w,"two")) return 2; if (!strcmp(w,"three")) return 3;
    if (!strcmp(w,"four")) return 4; if (!strcmp(w,"five")) return 5;
    if (!strcmp(w,"six")) return 6; if (!strcmp(w,"seven")) return 7;
    if (!strcmp(w,"eight")) return 8; return 9;
}

void sort_by_rank(char *line) {
    char toks[100][20]; int cnt=0;
    char *p = strtok(line, " ");
    while (p) { strcpy(toks[cnt++], p); p = strtok(NULL, " "); }
    for (int i=0;i<cnt-1;i++) for (int j=i+1;j<cnt;j++) if (numword_rank(toks[i])>numword_rank(toks[j])) { char tmp[20]; strcpy(tmp,toks[i]); strcpy(toks[i],toks[j]); strcpy(toks[j],tmp); }
    for (int i=0;i<cnt;i++) { printf("%s", toks[i]); if(i<cnt-1) printf(" "); }
    printf("\n");
}
