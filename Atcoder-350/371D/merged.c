#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int create_automaton_state(int *len, int *link, int *node_count, int length) {
    int state = (*node_count)++;
    len[state] = length;
    link[state] = -1;
    return state;
}

int extend_automaton_with_char(char c, int last, int transitions[200005][26], int *len, int *link, int *node_count) {
    int cur = create_automaton_state(len, link, node_count, len[last] + 1);
    int p = last;
    
    while (p != -1 && transitions[p][c - 'a'] == -1) {
        transitions[p][c - 'a'] = cur;
        p = link[p];
    }
    
    if (p == -1) {
        link[cur] = 0;
    } else {
        int q = transitions[p][c - 'a'];
        if (len[p] + 1 == len[q]) {
            link[cur] = q;
        } else {
            int clone = create_automaton_state(len, link, node_count, len[p] + 1);
            for (int i = 0; i < 26; i++) {
                transitions[clone][i] = transitions[q][i];
            }
            link[clone] = link[q];
            while (p != -1 && transitions[p][c - 'a'] == q) {
                transitions[p][c - 'a'] = clone;
                p = link[p];
            }
            link[q] = link[cur] = clone;
        }
    }
    return cur;
}

long long count_distinct_substrings(char *s, int transitions[200005][26], int *len, int *link) {
    int node_count = 1, last = 0;
    for (int i = 0; i < 200005; i++) {
        for (int j = 0; j < 26; j++) {
            transitions[i][j] = -1;
        }
    }
    
    for (int i = 0; s[i] != '\0'; i++) {
        last = extend_automaton_with_char(s[i], last, transitions, len, link, &node_count);
    }
    
    long long total = 0;
    for (int i = 1; i < node_count; i++) {
        total += len[i] - (link[i] == -1 ? 0 : len[link[i]]);
    }
    return total;
}

int main() {
    char s[100005];
    int transitions[200005][26], len[200005], link[200005];
    scanf("%s", s);
    printf("%lld\n", count_distinct_substrings(s, transitions, len, link));
    return 0;
}