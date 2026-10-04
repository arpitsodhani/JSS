#include <stdlib.h>


void read_input() {
#include <stdio.h>
#include <string.h>

char s[100005];
char t[100005];

void read_input() {
    scanf("%s", s);
    scanf("%s", t);
}

void find_positions() {
    int s_len = strlen(s);
    int t_len = strlen(t);
    int s_idx = 0;
    int t_idx = 0;
    
    while (s_idx < s_len && t_idx < t_len) {
        if (s[s_idx] == t[t_idx]) {
            printf("%d", t_idx + 1);
            s_idx++;
            if (s_idx < s_len) printf(" ");
        }
        t_idx++;
    }
    printf("\n");
}

int main() {
    read_input();
    find_positions();
    return 0;
}
}

void find_positions() {

}

int main() {

}

void read_input() {
#include <stdio.h>
#include <string.h>

char s[100005];
char t[100005];

void read_input() {
    scanf("%s", s);
    scanf("%s", t);
}

void find_positions() {
    int n = strlen(s);
    int m = strlen(t);
    int i = 0, j = 0;
    int first = 1;
    
    while (i < n && j < m) {
        if (s[i] == t[j]) {
            if (!first) printf(" ");
            printf("%d", j + 1);
            first = 0;
            i++;
        }
        j++;
    }
    printf("\n");
}

int main() {
    read_input();
    find_positions();
    return 0;
}
}

void find_positions() {

}

int main() {

}

void read_input() {
#include <stdio.h>
#include <string.h>

char s[100005];
char t[100005];

void read_input() {
    scanf("%s %s", s, t);
}

void find_positions() {
    int len_s = strlen(s), len_t = strlen(t);
    int pos_s = 0, pos_t = 0;
    
    while (pos_s < len_s && pos_t < len_t) {
        if (s[pos_s] == t[pos_t]) {
            if (pos_s > 0) printf(" ");
            printf("%d", pos_t + 1);
            pos_s++;
        }
        pos_t++;
    }
    printf("\n");
}

int main() {
    read_input();
    find_positions();
    return 0;
}
}

void find_positions() {

}

int main() {

}

void read_input() {
#include <stdio.h>
#include <string.h>

char s[100005];
char t[100005];

void read_input() {
    scanf("%s", s);
    scanf("%s", t);
}

void find_positions() {
    int slen = strlen(s), tlen = strlen(t);
    int si = 0, ti = 0, space = 0;
    
    for (ti = 0; ti < tlen && si < slen; ti++) {
        if (s[si] == t[ti]) {
            if (space) printf(" ");
            printf("%d", ti + 1);
            space = 1;
            si++;
        }
    }
    printf("\n");
}

int main() {
    read_input();
    find_positions();
    return 0;
}
}

void find_positions() {

}

int main() {

}

void read_input() {
#include <stdio.h>
#include <string.h>

char s[100005], t[100005];

void read_input() {
    scanf("%s %s", s, t);
}

void find_positions() {
    int ns = strlen(s), nt = strlen(t), is = 0, it = 0;
    while (is < ns && it < nt) {
        if (s[is] == t[it]) {
            if (is) printf(" ");
            printf("%d", it + 1);
            is++;
        }
        it++;
    }
    printf("\n");
}

int main() {
    read_input();
    find_positions();
    return 0;
}
}

void find_positions() {

}

int main() {

}
