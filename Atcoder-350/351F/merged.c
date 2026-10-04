#include <string.h>
#include <stdlib.h>


void read_input() {
#include <stdio.h>

int n;
long long a[300005];
long long sorted_a[300005];

void read_input() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &a[i]);
        sorted_a[i] = a[i];
    }
}

void sort_array() {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (sorted_a[j] > sorted_a[j+1]) {
                long long temp = sorted_a[j];
                sorted_a[j] = sorted_a[j+1];
                sorted_a[j+1] = temp;
            }
        }
    }
}

long long calculate_result() {
    long long answer = 0;
    long long prefix_sum[300005];
    prefix_sum[0] = sorted_a[0];
    
    for (int i = 1; i < n; i++) {
        prefix_sum[i] = prefix_sum[i-1] + sorted_a[i];
    }
    
    for (int i = 0; i < n; i++) {
        int pos = 0;
        for (int j = 0; j < n; j++) {
            if (sorted_a[j] < a[i]) pos++;
        }
        
        if (pos > 0) {
            answer += (long long)pos * a[i] - prefix_sum[pos-1];
        }
    }
    
    return answer;
}

int main() {
    read_input();
    sort_array();
    printf("%lld\n", calculate_result());
    return 0;
}
}

void sort_array() {

}

long long calculate_result() {

}

int main() {

}

void read_input() {
#include <stdio.h>

int n;
long long a[300005];
long long s[300005];

void read_input() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &a[i]);
        s[i] = a[i];
    }
}

void sort_array() {
    int swapped;
    do {
        swapped = 0;
        for (int i = 0; i < n - 1; i++) {
            if (s[i] > s[i+1]) {
                long long t = s[i];
                s[i] = s[i+1];
                s[i+1] = t;
                swapped = 1;
            }
        }
    } while (swapped);
}

long long calculate_result() {
    long long res = 0;
    long long cumsum[300005];
    cumsum[0] = s[0];
    for (int i = 1; i < n; i++) cumsum[i] = cumsum[i-1] + s[i];
    
    for (int i = 0; i < n; i++) {
        int cnt = 0;
        for (int j = 0; j < n; j++) {
            if (s[j] < a[i]) cnt++;
        }
        if (cnt > 0) {
            res += cnt * a[i] - cumsum[cnt-1];
        }
    }
    
    return res;
}

int main() {
    read_input();
    sort_array();
    printf("%lld\n", calculate_result());
    return 0;
}
}

void sort_array() {

}

long long calculate_result() {

}

int main() {

}

void read_input() {
#include <stdio.h>

int n;
long long a[300005], sorted[300005];

void read_input() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &a[i]);
        sorted[i] = a[i];
    }
}

void sort_array() {
    for (int pass = 0; pass < n; pass++) {
        for (int i = 0; i < n - 1; i++) {
            if (sorted[i] > sorted[i+1]) {
                long long swap = sorted[i];
                sorted[i] = sorted[i+1];
                sorted[i+1] = swap;
            }
        }
    }
}

long long calculate_result() {
    long long total = 0;
    long long psum[300005];
    psum[0] = sorted[0];
    for (int k = 1; k < n; k++) psum[k] = psum[k-1] + sorted[k];
    
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = 0; j < n; j++) {
            if (sorted[j] < a[i]) count++;
        }
        if (count > 0) {
            total += (long long)count * a[i] - psum[count-1];
        }
    }
    return total;
}

int main() {
    read_input();
    sort_array();
    printf("%lld\n", calculate_result());
    return 0;
}
}

void sort_array() {

}

long long calculate_result() {

}

int main() {

}

void read_input() {
#include <stdio.h>

int n;
long long a[300005], ord[300005];

void read_input() {
    scanf("%d", &n);
    int i = 0;
    while (i < n) {
        scanf("%lld", &a[i]);
        ord[i] = a[i];
        i++;
    }
}

void sort_array() {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (ord[j] < ord[minIdx]) minIdx = j;
        }
        if (minIdx != i) {
            long long tmp = ord[i];
            ord[i] = ord[minIdx];
            ord[minIdx] = tmp;
        }
    }
}

long long calculate_result() {
    long long ans = 0;
    long long sum[300005];
    sum[0] = ord[0];
    for (int i = 1; i < n; i++) sum[i] = sum[i-1] + ord[i];
    
    for (int i = 0; i < n; i++) {
        int less = 0;
        for (int j = 0; j < n; j++) {
            if (ord[j] < a[i]) less++;
        }
        if (less > 0) ans += less * a[i] - sum[less-1];
    }
    return ans;
}

int main() {
    read_input();
    sort_array();
    printf("%lld\n", calculate_result());
    return 0;
}
}

void sort_array() {

}

long long calculate_result() {

}

int main() {

}

void read_input() {
#include <stdio.h>

int n;
long long a[300005], b[300005];

void read_input() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) { scanf("%lld", &a[i]); b[i] = a[i]; }
}

void sort_array() {
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (b[i] > b[j]) {
                long long t = b[i]; b[i] = b[j]; b[j] = t;
            }
}

long long calculate_result() {
    long long r = 0, p[300005];
    p[0] = b[0];
    for (int i = 1; i < n; i++) p[i] = p[i-1] + b[i];
    for (int i = 0; i < n; i++) {
        int c = 0;
        for (int j = 0; j < n; j++) if (b[j] < a[i]) c++;
        if (c > 0) r += c * a[i] - p[c-1];
    }
    return r;
}

int main() {
    read_input();
    sort_array();
    printf("%lld\n", calculate_result());
    return 0;
}
}

void sort_array() {

}

long long calculate_result() {

}

int main() {

}
