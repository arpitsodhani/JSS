#include <stdlib.h>


void read_input() {
#include <stdio.h>
#include <string.h>

int h, w;
char grid[1005][1005];
int visited[1005][1005];
int magnet[1005][1005];
int queue_r[1000005], queue_c[1000005];
int front, rear;

void read_input() {
    scanf("%d %d", &h, &w);
    for (int i = 0; i < h; i++) {
        scanf("%s", grid[i]);
    }
    
    memset(magnet, 0, sizeof(magnet));
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (grid[i][j] == '#') {
                if (i > 0) magnet[i-1][j] = 1;
                if (i < h-1) magnet[i+1][j] = 1;
                if (j > 0) magnet[i][j-1] = 1;
                if (j < w-1) magnet[i][j+1] = 1;
            }
        }
    }
}

int bfs_component(int sr, int sc) {
    if (grid[sr][sc] == '#' || visited[sr][sc]) return 0;
    
    memset(visited, 0, sizeof(visited));
    front = rear = 0;
    queue_r[rear] = sr;
    queue_c[rear] = sc;
    rear++;
    visited[sr][sc] = 1;
    int count = 1;
    
    while (front < rear) {
        int r = queue_r[front];
        int c = queue_c[front];
        front++;
        
        int dr[] = {-1, 1, 0, 0};
        int dc[] = {0, 0, -1, 1};
        
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            
            if (nr >= 0 && nr < h && nc >= 0 && nc < w && 
                grid[nr][nc] == '.' && !visited[nr][nc] && !magnet[nr][nc]) {
                visited[nr][nc] = 1;
                queue_r[rear] = nr;
                queue_c[rear] = nc;
                rear++;
                count++;
            }
        }
    }
    
    int max_reach = count;
    for (int i = 0; i < rear; i++) {
        int r = queue_r[i];
        int c = queue_c[i];
        
        int dr[] = {-1, 1, 0, 0};
        int dc[] = {0, 0, -1, 1};
        
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            
            if (nr >= 0 && nr < h && nc >= 0 && nc < w && 
                grid[nr][nc] == '.' && magnet[nr][nc] && !visited[nr][nc]) {
                visited[nr][nc] = 1;
                max_reach++;
            }
        }
    }
    
    return max_reach;
}

int find_maximum() {
    int max_val = 0;
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (grid[i][j] == '.') {
                int val = bfs_component(i, j);
                if (val > max_val) max_val = val;
            }
        }
    }
    return max_val;
}

int main() {
    read_input();
    printf("%d\n", find_maximum());
    return 0;
}
}

int bfs_component(int, int) {

}

int find_maximum() {

}

int main() {

}

void read_input() {
#include <stdio.h>
#include <string.h>

int h, w;
char grid[1005][1005];
int vis[1005][1005];
int mag[1005][1005];
int qr[1000005], qc[1000005];
int f, r;

void read_input() {
    scanf("%d %d", &h, &w);
    for (int i = 0; i < h; i++) scanf("%s", grid[i]);
    
    memset(mag, 0, sizeof(mag));
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (grid[i][j] == '#') {
                if (i > 0 && grid[i-1][j] == '.') mag[i-1][j] = 1;
                if (i < h-1 && grid[i+1][j] == '.') mag[i+1][j] = 1;
                if (j > 0 && grid[i][j-1] == '.') mag[i][j-1] = 1;
                if (j < w-1 && grid[i][j+1] == '.') mag[i][j+1] = 1;
            }
        }
    }
}

int bfs_component(int sr, int sc) {
    if (grid[sr][sc] == '#' || vis[sr][sc]) return 0;
    
    memset(vis, 0, sizeof(vis));
    f = r = 0;
    qr[r] = sr; qc[r] = sc; r++;
    vis[sr][sc] = 1;
    int cnt = 1;
    
    while (f < r) {
        int row = qr[f], col = qc[f]; f++;
        int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
        
        for (int d = 0; d < 4; d++) {
            int nr = row + dirs[d][0];
            int nc = col + dirs[d][1];
            
            if (nr >= 0 && nr < h && nc >= 0 && nc < w && 
                grid[nr][nc] == '.' && !vis[nr][nc] && !mag[nr][nc]) {
                vis[nr][nc] = 1;
                qr[r] = nr; qc[r] = nc; r++;
                cnt++;
            }
        }
    }
    
    int result = cnt;
    for (int i = 0; i < r; i++) {
        int row = qr[i], col = qc[i];
        int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
        
        for (int d = 0; d < 4; d++) {
            int nr = row + dirs[d][0];
            int nc = col + dirs[d][1];
            
            if (nr >= 0 && nr < h && nc >= 0 && nc < w && 
                grid[nr][nc] == '.' && mag[nr][nc] && !vis[nr][nc]) {
                vis[nr][nc] = 1;
                result++;
            }
        }
    }
    
    return result;
}

int find_maximum() {
    int best = 0;
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (grid[i][j] == '.') {
                int v = bfs_component(i, j);
                if (v > best) best = v;
            }
        }
    }
    return best;
}

int main() {
    read_input();
    printf("%d\n", find_maximum());
    return 0;
}
}

int bfs_component(int, int) {

}

int find_maximum() {

}

int main() {

}

void read_input() {
#include <stdio.h>
#include <string.h>

int h, w;
char grid[1005][1005];
int seen[1005][1005];
int blocked[1005][1005];
int q_row[1000005], q_col[1000005];
int head, tail;

void read_input() {
    scanf("%d %d", &h, &w);
    int i, j;
    for (i = 0; i < h; i++) scanf("%s", grid[i]);
    
    memset(blocked, 0, sizeof(blocked));
    for (i = 0; i < h; i++) {
        for (j = 0; j < w; j++) {
            if (grid[i][j] == '#') {
                int di[] = {-1, 1, 0, 0};
                int dj[] = {0, 0, -1, 1};
                for (int k = 0; k < 4; k++) {
                    int ni = i + di[k], nj = j + dj[k];
                    if (ni >= 0 && ni < h && nj >= 0 && nj < w) {
                        blocked[ni][nj] = 1;
                    }
                }
            }
        }
    }
}

int bfs_component(int start_r, int start_c) {
    if (grid[start_r][start_c] == '#' || seen[start_r][start_c]) return 0;
    
    memset(seen, 0, sizeof(seen));
    head = tail = 0;
    q_row[tail] = start_r; q_col[tail] = start_c; tail++;
    seen[start_r][start_c] = 1;
    int total = 1;
    
    while (head < tail) {
        int r = q_row[head], c = q_col[head]; head++;
        int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};
        
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i], nc = c + dc[i];
            if (nr >= 0 && nr < h && nc >= 0 && nc < w && 
                grid[nr][nc] == '.' && !seen[nr][nc] && !blocked[nr][nc]) {
                seen[nr][nc] = 1;
                q_row[tail] = nr; q_col[tail] = nc; tail++;
                total++;
            }
        }
    }
    
    int reach = total;
    for (int i = 0; i < tail; i++) {
        int r = q_row[i], c = q_col[i];
        int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};
        for (int j = 0; j < 4; j++) {
            int nr = r + dr[j], nc = c + dc[j];
            if (nr >= 0 && nr < h && nc >= 0 && nc < w && 
                grid[nr][nc] == '.' && blocked[nr][nc] && !seen[nr][nc]) {
                seen[nr][nc] = 1;
                reach++;
            }
        }
    }
    
    return reach;
}

int find_maximum() {
    int answer = 0;
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (grid[i][j] == '.') {
                int val = bfs_component(i, j);
                if (val > answer) answer = val;
            }
        }
    }
    return answer;
}

int main() {
    read_input();
    printf("%d\n", find_maximum());
    return 0;
}
}

int bfs_component(int, int) {

}

int find_maximum() {

}

int main() {

}

void read_input() {
#include <stdio.h>
#include <string.h>

int h, w;
char grid[1005][1005];
int v[1005][1005];
int m[1005][1005];
int qr[1000005], qc[1000005];
int fp, rp;

void read_input() {
    scanf("%d %d", &h, &w);
    for (int i = 0; i < h; i++) scanf("%s", grid[i]);
    memset(m, 0, sizeof(m));
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (grid[i][j] == '#') {
                if (i > 0) m[i-1][j] = 1;
                if (i < h-1) m[i+1][j] = 1;
                if (j > 0) m[i][j-1] = 1;
                if (j < w-1) m[i][j+1] = 1;
            }
        }
    }
}

int bfs_component(int sr, int sc) {
    if (grid[sr][sc] != '.' || v[sr][sc]) return 0;
    memset(v, 0, sizeof(v));
    fp = rp = 0;
    qr[rp] = sr; qc[rp] = sc; rp++;
    v[sr][sc] = 1;
    int c = 1;
    
    while (fp < rp) {
        int r = qr[fp], co = qc[fp]; fp++;
        int d[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
        for (int k = 0; k < 4; k++) {
            int nr = r + d[k][0], nc = co + d[k][1];
            if (nr >= 0 && nr < h && nc >= 0 && nc < w && grid[nr][nc] == '.' && !v[nr][nc] && !m[nr][nc]) {
                v[nr][nc] = 1;
                qr[rp] = nr; qc[rp] = nc; rp++;
                c++;
            }
        }
    }
    
    int ans = c;
    for (int i = 0; i < rp; i++) {
        int r = qr[i], co = qc[i];
        int d[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
        for (int k = 0; k < 4; k++) {
            int nr = r + d[k][0], nc = co + d[k][1];
            if (nr >= 0 && nr < h && nc >= 0 && nc < w && grid[nr][nc] == '.' && m[nr][nc] && !v[nr][nc]) {
                v[nr][nc] = 1;
                ans++;
            }
        }
    }
    return ans;
}

int find_maximum() {
    int mx = 0;
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (grid[i][j] == '.') {
                int x = bfs_component(i, j);
                if (x > mx) mx = x;
            }
        }
    }
    return mx;
}

int main() {
    read_input();
    printf("%d\n", find_maximum());
    return 0;
}
}

int bfs_component(int, int) {

}

int find_maximum() {

}

int main() {

}

void read_input() {
#include <stdio.h>
#include <string.h>

int h, w;
char grid[1005][1005];
int vis[1005][1005], mag[1005][1005];
int qr[1000005], qc[1000005];

void read_input() {
    scanf("%d %d", &h, &w);
    for (int i = 0; i < h; i++) scanf("%s", grid[i]);
    memset(mag, 0, sizeof(mag));
    for (int i = 0; i < h; i++)
        for (int j = 0; j < w; j++)
            if (grid[i][j] == '#') {
                if (i>0) mag[i-1][j]=1;
                if (i<h-1) mag[i+1][j]=1;
                if (j>0) mag[i][j-1]=1;
                if (j<w-1) mag[i][j+1]=1;
            }
}

int bfs_component(int sr, int sc) {
    if (grid[sr][sc] != '.' || vis[sr][sc]) return 0;
    memset(vis, 0, sizeof(vis));
    int f=0, r=0, cnt=1;
    qr[r]=sr; qc[r]=sc; r++;
    vis[sr][sc]=1;
    while (f < r) {
        int row=qr[f], col=qc[f]; f++;
        int d[4][2]={{-1,0},{1,0},{0,-1},{0,1}};
        for (int k=0; k<4; k++) {
            int nr=row+d[k][0], nc=col+d[k][1];
            if (nr>=0 && nr<h && nc>=0 && nc<w && grid[nr][nc]=='.' && !vis[nr][nc] && !mag[nr][nc]) {
                vis[nr][nc]=1; qr[r]=nr; qc[r]=nc; r++; cnt++;
            }
        }
    }
    int res=cnt;
    for (int i=0; i<r; i++) {
        int row=qr[i], col=qc[i];
        int d[4][2]={{-1,0},{1,0},{0,-1},{0,1}};
        for (int k=0; k<4; k++) {
            int nr=row+d[k][0], nc=col+d[k][1];
            if (nr>=0 && nr<h && nc>=0 && nc<w && grid[nr][nc]=='.' && mag[nr][nc] && !vis[nr][nc]) {
                vis[nr][nc]=1; res++;
            }
        }
    }
    return res;
}

int find_maximum() {
    int mx=0;
    for (int i=0; i<h; i++)
        for (int j=0; j<w; j++)
            if (grid[i][j]=='.') {
                int v=bfs_component(i,j);
                if (v>mx) mx=v;
            }
    return mx;
}

int main() {
    read_input();
    printf("%d\n", find_maximum());
    return 0;
}
}

int bfs_component(int, int) {

}

int find_maximum() {

}

int main() {

}
