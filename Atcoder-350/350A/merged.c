#include <string.h>
#include <stdlib.h>
#include <stdio.h>


void read_id(char *s) { scanf("%s", s); }

int parse_num(char *s) { return (s[3]-'0')*100 + (s[4]-'0')*10 + (s[5]-'0'); }

int is_valid(int n) { return (n >= 1 && n <= 349 && n != 316); }

void print_yn(int ok) { printf("%s\n", ok ? "Yes" : "No"); }

int main() { char s[7]; read_id(s); print_yn(is_valid(parse_num(s))); return 0; }

int read_parse() { char buf[7]; scanf("%s", buf); int num = 0; for(int i = 3; i < 6; i++) num = num * 10 + (buf[i] - '0'); return num; }

int validate(int n) { return !(n < 1 || n > 349 || n == 316); }

void output_result(int v) { puts(v ? "Yes" : "No"); }

void get_input(char *str) { int i = 0, ch; while((ch = getchar()) != '\n' && ch != EOF) str[i++] = ch; str[i] = '\0'; }

int extract(char *s) { int r = 0; r += (s[3]-'0')*100; r += (s[4]-'0')*10; r += (s[5]-'0'); return r; }

int check_held(int num) { if(num == 316) return 0; return (num >= 1 && num <= 349); }

void write_ans(int ans) { printf("%s\n", ans ? "Yes" : "No"); }

int scan_convert() { char s[7]; scanf("%s", s); int n = 0, i = 3; while(i < 6) { n = n * 10 + (s[i]-'0'); i++; } return n; }

int verify_contest(int number) { return (number != 316 && number >= 1 && number <= 349); }

void output_verdict(int valid) { puts(valid ? "Yes" : "No"); }

int fast_read_num() { char buf[10]; scanf("%s", buf); return (buf[3]-'0')*100 + (buf[4]-'0')*10 + (buf[5]-'0'); }

int is_held(int n) { return !(n < 1 || n > 349 || n == 316); }

void write_result(int ans) { printf("%s\n", ans ? "Yes" : "No"); }
