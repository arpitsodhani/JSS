#include <string.h>


void initialize_dsu() {
#include <stdio.h>
#include <stdlib.h>

int parent[200005];
int rank_arr[200005];
int n, m;

void initialize_dsu() {
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
        rank_arr[i] = 0;
    }
}

int find_root(int x) {
    if (parent[x] != x) {
        parent[x] = find_root(parent[x]);
    }
    return parent[x];
}

void union_sets(int x, int y) {
    int rx = find_root(x);
    int ry = find_root(y);
    if (rx == ry) return;
    
    if (rank_arr[rx] < rank_arr[ry]) {
        parent[rx] = ry;
    } else if (rank_arr[rx] > rank_arr[ry]) {
        parent[ry] = rx;
    } else {
        parent[ry] = rx;
        rank_arr[rx]++;
    }
}

long long calculate_result() {
    int component_sizes[200005] = {0};
    for (int i = 1; i <= n; i++) {
        component_sizes[find_root(i)]++;
    }
    
    long long total_pairs = (long long)n * (n - 1) / 2;
    long long connected_pairs = m;
    
    for (int i = 1; i <= n; i++) {
        if (component_sizes[i] > 0) {
            long long sz = component_sizes[i];
            connected_pairs += sz * (sz - 1) / 2;
        }
    }
    
    return total_pairs - connected_pairs;
}

int main() {
    scanf("%d %d", &n, &m);
    initialize_dsu();
    
    for (int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        union_sets(a, b);
    }
    
    printf("%lld\n", calculate_result());
    return 0;
}
}

int find_root(int x) {

}

void union_sets(int x, int y) {

}

long long calculate_result() {

}

int main() {

}

void initialize_dsu() {
#include <stdio.h>
#include <stdlib.h>

int parent[200005];
int size[200005];
int n, m;

void initialize_dsu() {
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
        size[i] = 1;
    }
}

int find_root(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find_root(parent[x]);
}

void union_sets(int x, int y) {
    int rx = find_root(x);
    int ry = find_root(y);
    if (rx == ry) return;
    
    if (size[rx] < size[ry]) {
        parent[rx] = ry;
        size[ry] += size[rx];
    } else {
        parent[ry] = rx;
        size[rx] += size[ry];
    }
}

long long calculate_result() {
    long long total_possible = (long long)n * (n - 1) / 2;
    long long already_connected = 0;
    
    int visited[200005] = {0};
    for (int i = 1; i <= n; i++) {
        int root = find_root(i);
        if (!visited[root]) {
            visited[root] = 1;
            long long comp_size = size[root];
            already_connected += comp_size * (comp_size - 1) / 2;
        }
    }
    
    return total_possible - already_connected;
}

int main() {
    scanf("%d %d", &n, &m);
    initialize_dsu();
    
    for (int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        union_sets(a, b);
    }
    
    printf("%lld\n", calculate_result());
    return 0;
}
}

int find_root(int x) {

}

void union_sets(int x, int y) {

}

long long calculate_result() {

}

int main() {

}

void initialize_dsu() {
#include <stdio.h>
#include <stdlib.h>

int parent[200005];
int rank_arr[200005];
int n, m;

void initialize_dsu() {
    int i = 1;
    while (i <= n) {
        parent[i] = i;
        rank_arr[i] = 0;
        i++;
    }
}

int find_root(int x) {
    int root = x;
    while (parent[root] != root) {
        root = parent[root];
    }
    while (x != root) {
        int next = parent[x];
        parent[x] = root;
        x = next;
    }
    return root;
}

void union_sets(int x, int y) {
    int rx = find_root(x);
    int ry = find_root(y);
    if (rx != ry) {
        if (rank_arr[rx] < rank_arr[ry]) {
            parent[rx] = ry;
        } else if (rank_arr[rx] > rank_arr[ry]) {
            parent[ry] = rx;
        } else {
            parent[ry] = rx;
            rank_arr[rx]++;
        }
    }
}

long long calculate_result() {
    int comp_count[200005] = {0};
    for (int i = 1; i <= n; i++) {
        comp_count[find_root(i)]++;
    }
    
    long long max_friends = (long long)n * (n - 1) / 2;
    long long current_friends = 0;
    
    for (int i = 1; i <= n; i++) {
        if (comp_count[i] > 1) {
            long long s = comp_count[i];
            current_friends += s * (s - 1) / 2;
        }
    }
    
    return max_friends - current_friends;
}

int main() {
    scanf("%d %d", &n, &m);
    initialize_dsu();
    
    for (int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        union_sets(a, b);
    }
    
    printf("%lld\n", calculate_result());
    return 0;
}
}

int find_root(int x) {

}

void union_sets(int x, int y) {

}

long long calculate_result() {

}

int main() {

}

void initialize_dsu() {
#include <stdio.h>
#include <stdlib.h>

int parent[200005];
int rank_arr[200005];
int n, m;

void initialize_dsu() {
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
        rank_arr[i] = 1;
    }
}

int find_root(int x) {
    if (parent[x] == x) {
        return x;
    }
    int root = find_root(parent[x]);
    parent[x] = root;
    return root;
}

void union_sets(int x, int y) {
    int rootX = find_root(x);
    int rootY = find_root(y);
    
    if (rootX == rootY) return;
    
    if (rank_arr[rootX] >= rank_arr[rootY]) {
        parent[rootY] = rootX;
        rank_arr[rootX] += rank_arr[rootY];
    } else {
        parent[rootX] = rootY;
        rank_arr[rootY] += rank_arr[rootX];
    }
}

long long calculate_result() {
    long long answer = 0;
    long long total = (long long)n * (n - 1) / 2;
    
    int seen[200005] = {0};
    for (int i = 1; i <= n; i++) {
        int r = find_root(i);
        if (seen[r] == 0) {
            seen[r] = rank_arr[r];
        }
    }
    
    for (int i = 1; i <= n; i++) {
        if (seen[i] > 0) {
            long long cnt = seen[i];
            answer += cnt * (cnt - 1) / 2;
        }
    }
    
    return total - answer;
}

int main() {
    scanf("%d %d", &n, &m);
    initialize_dsu();
    
    for (int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        union_sets(a, b);
    }
    
    printf("%lld\n", calculate_result());
    return 0;
}
}

int find_root(int x) {

}

void union_sets(int x, int y) {

}

long long calculate_result() {

}

int main() {

}

void initialize_dsu() {
#include <stdio.h>
#include <stdlib.h>

int parent[200005];
int rank_arr[200005];
int n, m;

void initialize_dsu() {
    for (int i = 0; i <= n; i++) {
        parent[i] = i;
        rank_arr[i] = 0;
    }
}

int find_root(int x) {
    return parent[x] == x ? x : (parent[x] = find_root(parent[x]));
}

void union_sets(int x, int y) {
    x = find_root(x);
    y = find_root(y);
    if (x == y) return;
    
    if (rank_arr[x] < rank_arr[y]) {
        int temp = x; x = y; y = temp;
    }
    parent[y] = x;
    if (rank_arr[x] == rank_arr[y]) rank_arr[x]++;
}

long long calculate_result() {
    int sz[200005] = {0};
    for (int i = 1; i <= n; i++) {
        sz[find_root(i)]++;
    }
    
    long long total = (long long)n * (n - 1) / 2;
    long long connected = 0;
    for (int i = 1; i <= n; i++) {
        if (sz[i] > 0) {
            connected += (long long)sz[i] * (sz[i] - 1) / 2;
        }
    }
    
    return total - connected;
}

int main() {
    scanf("%d %d", &n, &m);
    initialize_dsu();
    
    for (int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        union_sets(a, b);
    }
    
    printf("%lld\n", calculate_result());
    return 0;
}
}

int find_root(int x) {

}

void union_sets(int x, int y) {

}

long long calculate_result() {

}

int main() {

}
