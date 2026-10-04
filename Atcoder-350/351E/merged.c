#include <string.h>


void read_input() {
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    long long x, y;
} Point;

Point points[200005];
int n;

void read_input() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld", &points[i].x, &points[i].y);
    }
}

long long abs_val(long long x) {
    return x < 0 ? -x : x;
}

long long calculate_result() {
    long long total = 0;
    
    for (int i = 0; i < n; i++) {
        points[i].x = points[i].x + points[i].y;
        points[i].y = points[i].x - 2 * points[i].y;
    }
    
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (points[j].x < points[i].x) {
                Point temp = points[i];
                points[i] = points[j];
                points[j] = temp;
            }
        }
    }
    
    for (int i = 0; i < n; i++) {
        total += (long long)(2 * i - n + 1) * points[i].x;
    }
    
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (points[j].y < points[i].y) {
                Point temp = points[i];
                points[i] = points[j];
                points[j] = temp;
            }
        }
    }
    
    for (int i = 0; i < n; i++) {
        total += (long long)(2 * i - n + 1) * points[i].y;
    }
    
    return total / 2;
}

int main() {
    read_input();
    printf("%lld\n", calculate_result());
    return 0;
}
}

long long abs_val(long long) {

}

long long calculate_result() {

}

int main() {

}

void read_input() {
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    long long x, y;
} Point;

Point pts[200005];
int n;

void read_input() {
    scanf("%d", &n);
    int i = 0;
    while (i < n) {
        scanf("%lld %lld", &pts[i].x, &pts[i].y);
        i++;
    }
}

long long abs_val(long long v) {
    return v >= 0 ? v : -v;
}

long long calculate_result() {
    long long answer = 0;
    
    for (int i = 0; i < n; i++) {
        long long sum = pts[i].x + pts[i].y;
        long long diff = pts[i].x - pts[i].y;
        pts[i].x = sum;
        pts[i].y = diff;
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (pts[i].x > pts[j].x) {
                Point t = pts[i];
                pts[i] = pts[j];
                pts[j] = t;
            }
        }
    }
    
    for (int i = 0; i < n; i++) {
        answer += pts[i].x * (2 * i - n + 1);
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (pts[i].y > pts[j].y) {
                Point t = pts[i];
                pts[i] = pts[j];
                pts[j] = t;
            }
        }
    }
    
    for (int i = 0; i < n; i++) {
        answer += pts[i].y * (2 * i - n + 1);
    }
    
    return answer / 2;
}

int main() {
    read_input();
    printf("%lld\n", calculate_result());
    return 0;
}
}

long long abs_val(long long) {

}

long long calculate_result() {

}

int main() {

}

void read_input() {
#include <stdio.h>
#include <stdlib.h>

typedef struct { long long x, y; } Point;
Point p[200005];
int n;

void read_input() {
    scanf("%d", &n);
    for (int k = 0; k < n; k++) scanf("%lld %lld", &p[k].x, &p[k].y);
}

long long abs_val(long long a) { return a < 0 ? -a : a; }

long long calculate_result() {
    long long res = 0;
    for (int i = 0; i < n; i++) {
        long long s = p[i].x + p[i].y, d = p[i].x - p[i].y;
        p[i].x = s; p[i].y = d;
    }
    
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - 1 - i; j++)
            if (p[j].x > p[j+1].x) {
                Point tmp = p[j]; p[j] = p[j+1]; p[j+1] = tmp;
            }
    
    for (int i = 0; i < n; i++) res += p[i].x * (2 * i - n + 1);
    
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - 1 - i; j++)
            if (p[j].y > p[j+1].y) {
                Point tmp = p[j]; p[j] = p[j+1]; p[j+1] = tmp;
            }
    
    for (int i = 0; i < n; i++) res += p[i].y * (2 * i - n + 1);
    
    return res / 2;
}

int main() {
    read_input();
    printf("%lld\n", calculate_result());
    return 0;
}
}

long long abs_val(long long) {

}

long long calculate_result() {

}

int main() {

}

void read_input() {
#include <stdio.h>
#include <stdlib.h>

typedef struct { long long x, y; } Point;
Point arr[200005];
int n;

void read_input() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%lld %lld", &arr[i].x, &arr[i].y);
}

long long abs_val(long long x) { return x < 0 ? -x : x; }

long long calculate_result() {
    long long sum = 0;
    
    for (int i = 0; i < n; i++) {
        long long a = arr[i].x + arr[i].y;
        long long b = arr[i].x - arr[i].y;
        arr[i].x = a; arr[i].y = b;
    }
    
    int swapped;
    do {
        swapped = 0;
        for (int i = 0; i < n - 1; i++) {
            if (arr[i].x > arr[i+1].x) {
                Point t = arr[i]; arr[i] = arr[i+1]; arr[i+1] = t;
                swapped = 1;
            }
        }
    } while (swapped);
    
    for (int i = 0; i < n; i++) sum += arr[i].x * (2 * i - n + 1);
    
    do {
        swapped = 0;
        for (int i = 0; i < n - 1; i++) {
            if (arr[i].y > arr[i+1].y) {
                Point t = arr[i]; arr[i] = arr[i+1]; arr[i+1] = t;
                swapped = 1;
            }
        }
    } while (swapped);
    
    for (int i = 0; i < n; i++) sum += arr[i].y * (2 * i - n + 1);
    
    return sum / 2;
}

int main() {
    read_input();
    printf("%lld\n", calculate_result());
    return 0;
}
}

long long abs_val(long long) {

}

long long calculate_result() {

}

int main() {

}

void read_input() {
#include <stdio.h>
#include <stdlib.h>

typedef struct { long long x, y; } Point;
Point data[200005];
int n;

void read_input() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%lld %lld", &data[i].x, &data[i].y);
}

long long abs_val(long long v) { return v < 0 ? -v : v; }

long long calculate_result() {
    long long total = 0;
    for (int i = 0; i < n; i++) {
        long long u = data[i].x + data[i].y, v = data[i].x - data[i].y;
        data[i].x = u; data[i].y = v;
    }
    
    for (int step = 0; step < n; step++)
        for (int i = 0; i < n - step - 1; i++)
            if (data[i].x > data[i+1].x) {
                Point swap = data[i]; data[i] = data[i+1]; data[i+1] = swap;
            }
    
    for (int i = 0; i < n; i++) total += data[i].x * (2 * i - n + 1);
    
    for (int step = 0; step < n; step++)
        for (int i = 0; i < n - step - 1; i++)
            if (data[i].y > data[i+1].y) {
                Point swap = data[i]; data[i] = data[i+1]; data[i+1] = swap;
            }
    
    for (int i = 0; i < n; i++) total += data[i].y * (2 * i - n + 1);
    
    return total / 2;
}

int main() {
    read_input();
    printf("%lld\n", calculate_result());
    return 0;
}
}

long long abs_val(long long) {

}

long long calculate_result() {

}

int main() {

}
