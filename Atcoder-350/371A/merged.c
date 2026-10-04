#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void insert_pattern_into_automaton(char *pattern, int trie[10005][26], int *is_end, int *node_count) {
    int current = 0;
    for (int i = 0; pattern[i] != '\0'; i++) {
        int c = pattern[i] - 'a';
        if (trie[current][c] == -1) {
            trie[current][c] = *node_count;
            for (int j = 0; j < 26; j++) {
                trie[*node_count][j] = -1;
            }
            (*node_count)++;
        }
        current = trie[current][c];
    }
    is_end[current] = 1;
}

void build_failure_links_bfs(int trie[10005][26], int *fail, int node_count) {
    int queue[10005], front = 0, rear = 0;
    for (int c = 0; c < 26; c++) {
        if (trie[0][c] != -1) {
            fail[trie[0][c]] = 0;
            queue[rear++] = trie[0][c];
        } else {
            trie[0][c] = 0;
        }
    }
    
    while (front < rear) {
        int state = queue[front++];
        for (int c = 0; c < 26; c++) {
            if (trie[state][c] != -1) {
                int failure = fail[state];
                while (trie[failure][c] == -1) {
                    failure = fail[failure];
                }
                fail[trie[state][c]] = trie[failure][c];
                queue[rear++] = trie[state][c];
            }
        }
    }
}

int search_text_with_automaton(char *text, int trie[10005][26], int *fail, int *is_end) {
    int state = 0, matches = 0;
    for (int i = 0; text[i] != '\0'; i++) {
        int c = text[i] - 'a';
        while (trie[state][c] == -1) {
            state = fail[state];
        }
        state = trie[state][c];
        if (is_end[state]) matches++;
    }
    return matches;
}

int main() {
    int n, trie[10005][26], is_end[10005] = {0}, fail[10005] = {0}, node_count = 1;
    char patterns[105][105], text[100005];
    
    for (int i = 0; i < 10005; i++) {
        for (int j = 0; j < 26; j++) {
            trie[i][j] = -1;
        }
    }
    
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", patterns[i]);
        insert_pattern_into_automaton(patterns[i], trie, is_end, &node_count);
    }
    
    build_failure_links_bfs(trie, fail, node_count);
    scanf("%s", text);
    printf("%d\n", search_text_with_automaton(text, trie, fail, is_end));
    return 0;
}