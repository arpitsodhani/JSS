#include <string.h>
#include <stdlib.h>


void read_input() {
#include <stdio.h>

int n;
char grid1[105][105];
char grid2[105][105];

void read_input() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", grid1[i]);
    }
    for (int i = 0; i < n; i++) {
        scanf("%s", grid2[i]);
    }
}

void find_difference() {
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < n; col++) {
            if (grid1[row][col] != grid2[row][col]) {
                printf("%d %d\n", row + 1, col + 1);
                return;
            }
        }
    }
}

int main() {
    read_input();
    find_difference();
    return 0;
}
}

void find_difference() {

}

int main() {

}

void read_input() {
#include <stdio.h>

int n;
char grid1[105][105];
char grid2[105][105];

void read_input() {
    scanf("%d", &n);
    int i = 0;
    while (i < n) {
        scanf("%s", grid1[i]);
        i++;
    }
    i = 0;
    while (i < n) {
        scanf("%s", grid2[i]);
        i++;
    }
}

void find_difference() {
    int r, c;
    for (r = 0; r < n; r++) {
        for (c = 0; c < n; c++) {
            if (grid1[r][c] != grid2[r][c]) {
                printf("%d %d\n", r + 1, c + 1);
                return;
            }
        }
    }
}

int main() {
    read_input();
    find_difference();
    return 0;
}
}

void find_difference() {

}

int main() {

}

void read_input() {
#include <stdio.h>

int n;
char grid1[105][105];
char grid2[105][105];

void read_input() {
    scanf("%d", &n);
    for (int k = 0; k < n; k++) scanf("%s", grid1[k]);
    for (int k = 0; k < n; k++) scanf("%s", grid2[k]);
}

void find_difference() {
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (grid1[i][j] != grid2[i][j]) {
                printf("%d %d\n", i + 1, j + 1);
                return;
            }
        }
    }
}

int main() {
    read_input();
    find_difference();
    return 0;
}
}

void find_difference() {

}

int main() {

}

void read_input() {
#include <stdio.h>

int n;
char grid1[105][105];
char grid2[105][105];

void read_input() {
    scanf("%d", &n);
    for (int idx = 0; idx < n; idx++) {
        scanf("%s", grid1[idx]);
    }
    for (int idx = 0; idx < n; idx++) {
        scanf("%s", grid2[idx]);
    }
}

void find_difference() {
    for (int x = 0; x < n; x++) {
        for (int y = 0; y < n; y++) {
            if (grid1[x][y] != grid2[x][y]) {
                printf("%d %d\n", x + 1, y + 1);
                return;
            }
        }
    }
}

int main() {
    read_input();
    find_difference();
    return 0;
}
}

void find_difference() {

}

int main() {

}

void read_input() {
#include <stdio.h>

int n;
char grid1[105][105];
char grid2[105][105];

void read_input() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%s", grid1[i]);
    for (int i = 0; i < n; i++) scanf("%s", grid2[i]);
}

void find_difference() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (grid1[i][j] != grid2[i][j]) {
                printf("%d %d\n", i + 1, j + 1);
                return;
            }
        }
    }
}

int main() {
    read_input();
    find_difference();
    return 0;
}
}

void find_difference() {

}

int main() {

}
