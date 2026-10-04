#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void read_configurations(int *n, char *s, char *t) {
    scanf("%d", n);
    scanf("%s", s);
    scanf("%s", t);
}

long long encode_state(int n, char *config, int empty_pos) {
    long long hash = 0;
    for (int i = 0; i < n; i++) {
        hash = hash * 3 + (config[i] == 'W' ? 1 : (config[i] == 'B' ? 2 : 0));
    }
    return hash * 100 + empty_pos;
}

int bfs_minimum_moves(int n, char *s, char *t) {
    long long start = encode_state(n, s, n);
    long long target = encode_state(n, t, n);
    if (start == target) return 0;
    long long queue[100000], visited[100000];
    int dist[100000];
    int head = 0, tail = 0, vis_cnt = 0;
    queue[tail++] = start;
    visited[vis_cnt++] = start;
    dist[0] = 0;
    while (head < tail) {
        long long curr = queue[head];
        int d = dist[head];
        head++;
        char state[20];
        int emp = curr % 100;
        long long tmp = curr / 100;
        for (int i = n - 1; i >= 0; i--) {
            state[i] = (tmp % 3 == 1 ? 'W' : (tmp % 3 == 2 ? 'B' : '.'));
            tmp /= 3;
        }
        for (int i = 0; i <= n; i++) {
            if (i == emp || i + 1 == emp) continue;
            char new_state[20];
            for (int j = 0; j < n; j++) new_state[j] = state[j];
            new_state[emp] = state[i];
            new_state[emp + 1] = state[i + 1];
            new_state[i] = '.';
            new_state[i + 1] = '.';
            long long next = encode_state(n, new_state, i);
            int found = 0;
            for (int j = 0; j < vis_cnt; j++) {
                if (visited[j] == next) {
                    found = 1;
                    break;
                }
            }
            if (!found) {
                if (next == target) return d + 1;
                queue[tail] = next;
                dist[tail] = d + 1;
                tail++;
                visited[vis_cnt++] = next;
            }
        }
    }
    return -1;
}

int main() {
    int n;
    char s[20], t[20];
    read_configurations(&n, s, t);
    printf("%d\n", bfs_minimum_moves(n, s, t));
    return 0;
}

