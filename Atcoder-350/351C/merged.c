#include <string.h>
#include <stdlib.h>


void read_input() {
#include <stdio.h>

long long stack[500005];
int top;
int n;

void read_input() {
    scanf("%d", &n);
    top = 0;
}

void process_stones() {
    for (int i = 0; i < n; i++) {
        long long a;
        scanf("%lld", &a);
        
        stack[top++] = a;
        
        while (top >= 2 && stack[top-1] == stack[top-2]) {
            long long merged = stack[top-1] + 1;
            top -= 2;
            stack[top++] = merged;
        }
    }
}

void output_result() {
    printf("%d\n", top);
}

int main() {
    read_input();
    process_stones();
    output_result();
    return 0;
}
}

void process_stones() {

}

void output_result() {

}

int main() {

}

void read_input() {
#include <stdio.h>

long long stk[500005];
int ptr;
int n;

void read_input() {
    scanf("%d", &n);
    ptr = 0;
}

void process_stones() {
    for (int j = 0; j < n; j++) {
        long long val;
        scanf("%lld", &val);
        stk[ptr++] = val;
        
        while (ptr > 1 && stk[ptr-1] == stk[ptr-2]) {
            long long new_val = stk[ptr-1] + 1;
            ptr--;
            ptr--;
            stk[ptr++] = new_val;
        }
    }
}

void output_result() {
    printf("%d\n", ptr);
}

int main() {
    read_input();
    process_stones();
    output_result();
    return 0;
}
}

void process_stones() {

}

void output_result() {

}

int main() {

}

void read_input() {
#include <stdio.h>

long long arr[500005];
int sz;
int n;

void read_input() {
    scanf("%d", &n);
    sz = 0;
}

void process_stones() {
    int i = 0;
    while (i < n) {
        long long x;
        scanf("%lld", &x);
        arr[sz++] = x;
        
        while (sz >= 2 && arr[sz-1] == arr[sz-2]) {
            long long combined = arr[sz-1] + 1;
            sz -= 2;
            arr[sz++] = combined;
        }
        i++;
    }
}

void output_result() {
    printf("%d\n", sz);
}

int main() {
    read_input();
    process_stones();
    output_result();
    return 0;
}
}

void process_stones() {

}

void output_result() {

}

int main() {

}

void read_input() {
#include <stdio.h>

long long pile[500005];
int count;
int n;

void read_input() {
    scanf("%d", &n);
    count = 0;
}

void process_stones() {
    for (int k = 0; k < n; k++) {
        long long stone;
        scanf("%lld", &stone);
        pile[count++] = stone;
        
        while (count > 1 && pile[count-1] == pile[count-2]) {
            long long merge = pile[count-1] + 1;
            count--;
            count--;
            pile[count++] = merge;
        }
    }
}

void output_result() {
    printf("%d\n", count);
}

int main() {
    read_input();
    process_stones();
    output_result();
    return 0;
}
}

void process_stones() {

}

void output_result() {

}

int main() {

}

void read_input() {
#include <stdio.h>

long long s[500005];
int sp;
int n;

void read_input() {
    scanf("%d", &n);
    sp = 0;
}

void process_stones() {
    for (int i = 0; i < n; i++) {
        long long v;
        scanf("%lld", &v);
        s[sp++] = v;
        while (sp >= 2 && s[sp-1] == s[sp-2]) {
            long long m = s[sp-1] + 1;
            sp -= 2;
            s[sp++] = m;
        }
    }
}

void output_result() {
    printf("%d\n", sp);
}

int main() {
    read_input();
    process_stones();
    output_result();
    return 0;
}
}

void process_stones() {

}

void output_result() {

}

int main() {

}
