#include <string.h>
#include <stdlib.h>


void read_input() {
#include <stdio.h>

int n, x, y, z;

void read_input() {
    scanf("%d %d %d %d", &n, &x, &y, &z);
}

int check_condition() {
    if (x < y) {
        if (z >= x && z <= y) return 1;
    } else {
        if (z >= y && z <= x) return 1;
    }
    return 0;
}

int main() {
    read_input();
    if (check_condition()) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }
    return 0;
}
}

int check_condition() {

}

int main() {

}

void read_input() {
#include <stdio.h>

int n, x, y, z;

void read_input() {
    scanf("%d %d %d %d", &n, &x, &y, &z);
}

int check_condition() {
    int min = x < y ? x : y;
    int max = x > y ? x : y;
    return (z >= min && z <= max) ? 1 : 0;
}

int main() {
    read_input();
    printf("%s\n", check_condition() ? "Yes" : "No");
    return 0;
}
}

int check_condition() {

}

int main() {

}

void read_input() {
#include <stdio.h>

int n, x, y, z;

void read_input() {
    scanf("%d %d %d %d", &n, &x, &y, &z);
}

int check_condition() {
    int lower, upper;
    if (x <= y) {
        lower = x;
        upper = y;
    } else {
        lower = y;
        upper = x;
    }
    return z >= lower && z <= upper;
}

int main() {
    read_input();
    if (check_condition()) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }
    return 0;
}
}

int check_condition() {

}

int main() {

}

void read_input() {
#include <stdio.h>

int n, x, y, z;

void read_input() {
    scanf("%d %d %d %d", &n, &x, &y, &z);
}

int check_condition() {
    if ((x <= z && z <= y) || (y <= z && z <= x)) {
        return 1;
    }
    return 0;
}

int main() {
    read_input();
    int result = check_condition();
    if (result) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }
    return 0;
}
}

int check_condition() {

}

int main() {

}

void read_input() {
#include <stdio.h>

int n, x, y, z;

void read_input() {
    scanf("%d %d %d %d", &n, &x, &y, &z);
}

int check_condition() {
    int a = x, b = y;
    if (a > b) { int t = a; a = b; b = t; }
    return (z >= a && z <= b) ? 1 : 0;
}

int main() {
    read_input();
    printf("%s\n", check_condition() ? "Yes" : "No");
    return 0;
}
}

int check_condition() {

}

int main() {

}
