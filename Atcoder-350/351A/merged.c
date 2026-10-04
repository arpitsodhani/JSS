#include <string.h>
#include <stdlib.h>


void read_input() {
#include <stdio.h>

int team_a[9];
int team_b[8];

void read_input() {
    for (int i = 0; i < 9; i++) {
        scanf("%d", &team_a[i]);
    }
    for (int i = 0; i < 8; i++) {
        scanf("%d", &team_b[i]);
    }
}

int calculate_result() {
    int sum_a = 0;
    for (int i = 0; i < 9; i++) {
        sum_a += team_a[i];
    }
    
    int sum_b = 0;
    for (int i = 0; i < 8; i++) {
        sum_b += team_b[i];
    }
    
    return sum_b - sum_a + 1;
}

int main() {
    read_input();
    printf("%d\n", calculate_result());
    return 0;
}
}

int calculate_result() {

}

int main() {

}

void read_input() {
#include <stdio.h>

int team_a[9];
int team_b[8];

void read_input() {
    int i = 0;
    while (i < 9) {
        scanf("%d", &team_a[i]);
        i++;
    }
    i = 0;
    while (i < 8) {
        scanf("%d", &team_b[i]);
        i++;
    }
}

int calculate_result() {
    int total_a = 0;
    int idx = 0;
    while (idx < 9) {
        total_a += team_a[idx];
        idx++;
    }
    
    int total_b = 0;
    idx = 0;
    while (idx < 8) {
        total_b += team_b[idx];
        idx++;
    }
    
    int needed = total_b - total_a + 1;
    return needed;
}

int main() {
    read_input();
    printf("%d\n", calculate_result());
    return 0;
}
}

int calculate_result() {

}

int main() {

}

void read_input() {
#include <stdio.h>

int team_a[9];
int team_b[8];

void read_input() {
    for (int j = 0; j < 9; j++) scanf("%d", &team_a[j]);
    for (int j = 0; j < 8; j++) scanf("%d", &team_b[j]);
}

int calculate_result() {
    int score_a = 0, score_b = 0;
    
    for (int j = 0; j < 9; j++) {
        score_a += team_a[j];
    }
    
    for (int j = 0; j < 8; j++) {
        score_b += team_b[j];
    }
    
    return score_b - score_a + 1;
}

int main() {
    read_input();
    printf("%d\n", calculate_result());
    return 0;
}
}

int calculate_result() {

}

int main() {

}

void read_input() {
#include <stdio.h>

int team_a[9];
int team_b[8];

void read_input() {
    for (int k = 0; k < 9; k++) {
        scanf("%d", team_a + k);
    }
    for (int k = 0; k < 8; k++) {
        scanf("%d", team_b + k);
    }
}

int calculate_result() {
    int a = 0, b = 0, i;
    for (i = 0; i < 9; i++) a += team_a[i];
    for (i = 0; i < 8; i++) b += team_b[i];
    return b - a + 1;
}

int main() {
    read_input();
    printf("%d\n", calculate_result());
    return 0;
}
}

int calculate_result() {

}

int main() {

}

void read_input() {
#include <stdio.h>

int team_a[9];
int team_b[8];

void read_input() {
    int i;
    for (i = 0; i < 9; i++) scanf("%d", &team_a[i]);
    for (i = 0; i < 8; i++) scanf("%d", &team_b[i]);
}

int calculate_result() {
    int sum1 = 0, sum2 = 0;
    for (int i = 0; i < 9; i++) sum1 += team_a[i];
    for (int i = 0; i < 8; i++) sum2 += team_b[i];
    return sum2 - sum1 + 1;
}

int main() {
    read_input();
    printf("%d\n", calculate_result());
    return 0;
}
}

int calculate_result() {

}

int main() {

}
