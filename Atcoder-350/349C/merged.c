

void read_input(char *s, char *t) { scanf("%s%s", s, t); }

int check_match(char *s, char *t) { int j = 0; for(int i = 0; s[i] && j < 3; i++) { if(t[j] == 'X') break; if(s[i] - 'a' == t[j] - 'A') j++; } return (j == 3 || (j == 2 && t[2] == 'X')); }

void output(int ok) { puts(ok ? "Yes" : "No"); }

int main() { char s[100001], t[4]; read_input(s, t); output(check_match(s, t)); return 0; }

void get_strings(char *s, char *t) { scanf("%s%s", s, t); }

int validate_code(char *s, char *t) { int pos = 0, matched = 0; while(s[pos] && matched < 3) { if(t[matched] == 'X') break; if((s[pos] | 32) == (t[matched] | 32)) matched++; pos++; } return matched == 3 || (matched == 2 && t[2] == 'X'); }

void print_result(int res) { printf("%s\n", res ? "Yes" : "No"); }

void input_data(char *a, char *b) { scanf("%s%s", a, b); }

int is_airport_code(char *str, char *code) { int i = 0, cnt = 0; for(int k = 0; str[k]; k++) { if(cnt < 3 && code[cnt] == 'X') break; if(cnt < 3 && str[k] + ('A'-'a') == code[cnt]) cnt++; } return cnt >= 2 && (cnt == 3 || code[2] == 'X'); }

void write_ans(int v) { puts(v ? "Yes" : "No"); }

void scan_input(char *s, char *t) { scanf("%s%s", s, t); }

int match_subsequence(char *s, char *t) { int idx = 0, found = 0; for(; s[idx]; idx++) { if(found == 2 && t[2] == 'X') return 1; if(found < 3 && (s[idx]-'a') == (t[found]-'A')) found++; if(found == 3) return 1; } return found == 2 && t[2] == 'X'; }

void output_result(int ans) { printf("%s\n", ans ? "Yes" : "No"); }

void read_two_strings(char *s, char *t) { scanf("%s%s", s, t); }

int check_airport(char *s, char *t) { int m = 0; for(int i = 0; s[i] && m < 3; i++) { if(m < 3 && t[m] == 'X') { m = 2; break; } if((s[i] & ~32) == t[m]) m++; } return m == 3 || (m == 2 && t[2] == 'X'); }

void print_yn(int ok) { puts(ok ? "Yes" : "No"); }
