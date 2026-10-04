#include <stdlib.h>


void initialize_parser() {
#include <stdio.h>
#include <string.h>
#include <ctype.h>

char s[500005];
char result[500005];
int stack[500005];
int sp;

void initialize_parser() {
    sp = 0;
}

void process_string() {
    int len = strlen(s);
    int pos = 0;
    int uppercase = 0;
    
    for (int i = 0; i < len; i++) {
        if (s[i] == '(') {
            stack[sp++] = pos;
            stack[sp++] = uppercase;
        } else if (s[i] == ')') {
            uppercase = stack[--sp];
            int start = stack[--sp];
            int end = pos - 1;
            while (start < end) {
                char tmp = result[start];
                result[start] = result[end];
                result[end] = tmp;
                start++;
                end--;
            }
        } else {
            char ch = s[i];
            if (uppercase) {
                result[pos++] = isupper(ch) ? tolower(ch) : toupper(ch);
            } else {
                result[pos++] = ch;
            }
        }
    }
    result[pos] = '\0';
}

void output_result() {
    printf("%s\n", result);
}

int main() {
    scanf("%s", s);
    initialize_parser();
    process_string();
    output_result();
    return 0;
}
}

void process_string() {

}

void output_result() {

}

int main() {

}

void initialize_parser() {
#include <stdio.h>
#include <string.h>
#include <ctype.h>

char s[500005];
char result[500005];
int stk[500005];
int top;

void initialize_parser() {
    top = 0;
}

void process_string() {
    int n = strlen(s);
    int write_pos = 0;
    int flip = 0;
    
    for (int i = 0; i < n; i++) {
        if (s[i] == '(') {
            stk[top++] = write_pos;
            stk[top++] = flip;
            flip = 1 - flip;
        } else if (s[i] == ')') {
            flip = stk[--top];
            int left = stk[--top];
            int right = write_pos - 1;
            while (left < right) {
                char t = result[left];
                result[left++] = result[right];
                result[right--] = t;
            }
        } else {
            if (flip) {
                result[write_pos++] = islower(s[i]) ? toupper(s[i]) : tolower(s[i]);
            } else {
                result[write_pos++] = s[i];
            }
        }
    }
    result[write_pos] = '\0';
}

void output_result() {
    printf("%s\n", result);
}

int main() {
    scanf("%s", s);
    initialize_parser();
    process_string();
    output_result();
    return 0;
}
}

void process_string() {

}

void output_result() {

}

int main() {

}

void initialize_parser() {
#include <stdio.h>
#include <string.h>
#include <ctype.h>

char s[500005];
char result[500005];
int position_stack[500005];
int case_stack[500005];
int stack_ptr;

void initialize_parser() {
    stack_ptr = 0;
}

void process_string() {
    int length = strlen(s);
    int idx = 0;
    int should_flip = 0;
    
    int i = 0;
    while (i < length) {
        if (s[i] == '(') {
            position_stack[stack_ptr] = idx;
            case_stack[stack_ptr] = should_flip;
            stack_ptr++;
            should_flip = !should_flip;
        } else if (s[i] == ')') {
            stack_ptr--;
            should_flip = case_stack[stack_ptr];
            int begin = position_stack[stack_ptr];
            int finish = idx - 1;
            while (begin < finish) {
                char temp = result[begin];
                result[begin] = result[finish];
                result[finish] = temp;
                begin++;
                finish--;
            }
        } else {
            if (should_flip) {
                if (isupper(s[i])) {
                    result[idx++] = tolower(s[i]);
                } else {
                    result[idx++] = toupper(s[i]);
                }
            } else {
                result[idx++] = s[i];
            }
        }
        i++;
    }
    result[idx] = '\0';
}

void output_result() {
    printf("%s\n", result);
}

int main() {
    scanf("%s", s);
    initialize_parser();
    process_string();
    output_result();
    return 0;
}
}

void process_string() {

}

void output_result() {

}

int main() {

}

void initialize_parser() {
#include <stdio.h>
#include <string.h>
#include <ctype.h>

char s[500005];
char result[500005];
int st[500005];
int ptr;

void initialize_parser() {
    ptr = 0;
}

void process_string() {
    int len = strlen(s);
    int out = 0;
    int toggle = 0;
    
    for (int k = 0; k < len; k++) {
        char c = s[k];
        if (c == '(') {
            st[ptr++] = out;
            st[ptr++] = toggle;
            toggle ^= 1;
        } else if (c == ')') {
            toggle = st[--ptr];
            int l = st[--ptr];
            int r = out - 1;
            while (l < r) {
                char swap = result[l];
                result[l] = result[r];
                result[r] = swap;
                l++; r--;
            }
        } else {
            if (toggle) {
                result[out++] = isupper(c) ? tolower(c) : toupper(c);
            } else {
                result[out++] = c;
            }
        }
    }
    result[out] = '\0';
}

void output_result() {
    printf("%s\n", result);
}

int main() {
    scanf("%s", s);
    initialize_parser();
    process_string();
    output_result();
    return 0;
}
}

void process_string() {

}

void output_result() {

}

int main() {

}

void initialize_parser() {
#include <stdio.h>
#include <string.h>
#include <ctype.h>

char s[500005];
char result[500005];
int pos_stk[500005], case_stk[500005], sp;

void initialize_parser() {
    sp = 0;
}

void process_string() {
    int n = strlen(s), p = 0, flip = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '(') {
            pos_stk[sp] = p;
            case_stk[sp++] = flip;
            flip ^= 1;
        } else if (s[i] == ')') {
            flip = case_stk[--sp];
            int a = pos_stk[sp], b = p - 1;
            while (a < b) {
                char t = result[a]; result[a++] = result[b]; result[b--] = t;
            }
        } else {
            result[p++] = flip ? (isupper(s[i]) ? tolower(s[i]) : toupper(s[i])) : s[i];
        }
    }
    result[p] = '\0';
}

void output_result() {
    printf("%s\n", result);
}

int main() {
    scanf("%s", s);
    initialize_parser();
    process_string();
    output_result();
    return 0;
}
}

void process_string() {

}

void output_result() {

}

int main() {

}
