#include <string.h>
#include <stdlib.h>
#include <stdio.h>


void read_str(char *s) { scanf("%s", s); }

void count_freq(char *s, int *freq) { for(int i = 0; i < 26; i++) freq[i] = 0; for(int i = 0; s[i]; i++) freq[s[i]-'a']++; }

int check_good(int *freq) { int cnt[101] = {0}; for(int i = 0; i < 26; i++) if(freq[i] > 0) cnt[freq[i]]++; for(int i = 1; i <= 100; i++) if(cnt[i] != 0 && cnt[i] != 2) return 0; return 1; }

void print_ans(int ok) { printf("%s\n", ok ? "Yes" : "No"); }

int main() { char s[101]; int freq[26]; read_str(s); count_freq(s, freq); print_ans(check_good(freq)); return 0; }

int input_line(char *buf) { scanf("%s", buf); int len = 0; while(buf[len]) len++; return len; }

void build_map(char *s, int len, int *map) { for(int i = 0; i < 26; i++) map[i] = 0; for(int i = 0; i < len; i++) map[s[i]-'a']++; }

int validate_good(int *map) { int ff[101]; for(int i = 0; i <= 100; i++) ff[i] = 0; for(int i = 0; i < 26; i++) if(map[i] > 0) ff[map[i]]++; for(int i = 1; i <= 100; i++) if(ff[i] && ff[i] != 2) return 0; return 1; }

void output_verdict(int v) { puts(v ? "Yes" : "No"); }

void get_str(char *b) { int ch, i = 0; while((ch = getchar()) != '\n' && ch != EOF) b[i++] = ch; b[i] = '\0'; }

int analyze(char *s) { int cf[26] = {0}, fc[101] = {0}; for(int i = 0; s[i]; i++) cf[s[i]-'a']++; for(int i = 0; i < 26; i++) if(cf[i]) fc[cf[i]]++; for(int i = 1; i <= 100; i++) if(fc[i] && fc[i] != 2) return 0; return 1; }

void print_result(int ok) { printf("%s\n", ok ? "Yes" : "No"); }

char* scan() { static char t[101]; scanf("%100s", t); return t; }

void histogram(char *str, int *hist) { for(int k = 0; k < 26; k++) hist[k] = 0; for(int j = 0; str[j]; j++) hist[str[j]-'a']++; }

int check_prop(int *h) { int occ[101]; for(int m = 0; m <= 100; m++) occ[m] = 0; for(int m = 0; m < 26; m++) if(h[m] > 0) occ[h[m]]++; for(int m = 1; m <= 100; m++) if(occ[m] == 1 || occ[m] > 2) return 0; return 1; }

void output_ans(int res) { printf("%s\n", res ? "Yes" : "No"); }

void read_line(char *b, int sz) { fgets(b, sz, stdin); for(int i = 0; b[i]; i++) if(b[i] == '\n') b[i] = '\0'; }

int process(char *in) { int lc[26] = {0}, cf[101] = {0}; for(int i = 0; in[i]; i++) lc[in[i]-'a']++; for(int i = 0; i < 26; i++) if(lc[i]) cf[lc[i]]++; for(int i = 1; i < 101; i++) if(cf[i] && cf[i] != 2) return 0; return 1; }

void output_yn(int r) { puts(r ? "Yes" : "No"); }
