

void read_grid(int grid[3][3]) { for(int i = 0; i < 3; i++) for(int j = 0; j < 3; j++) scanf("%d", &grid[i][j]); }

int check_win(int g[3][3], int p) { for(int i = 0; i < 3; i++) if(g[i][0]==p && g[i][1]==p && g[i][2]==p) return 1; for(int j = 0; j < 3; j++) if(g[0][j]==p && g[1][j]==p && g[2][j]==p) return 1; if(g[0][0]==p && g[1][1]==p && g[2][2]==p) return 1; if(g[0][2]==p && g[1][1]==p && g[2][0]==p) return 1; return 0; }

int minimax(int g[3][3], int turn) { if(check_win(g,1)) return 1; if(check_win(g,2)) return -1; int empty = 0; for(int i = 0; i < 3; i++) for(int j = 0; j < 3; j++) if(g[i][j] == 0) empty++; if(empty == 0) return 0; int best = turn == 1 ? -2 : 2; for(int i = 0; i < 3; i++) for(int j = 0; j < 3; j++) if(g[i][j] == 0) { g[i][j] = turn; int val = minimax(g, 3-turn); g[i][j] = 0; if(turn == 1) { if(val > best) best = val; } else { if(val < best) best = val; } } return best; }

void output(int res) { if(res > 0) puts("Takahashi"); else if(res < 0) puts("Aoki"); else puts("Draw"); }

int main() { int grid[3][3]; read_grid(grid); int res = minimax(grid, 1); output(res); return 0; }

void input_board(int b[3][3]) { for(int r = 0; r < 3; r++) for(int c = 0; c < 3; c++) scanf("%d", &b[r][c]); }

int has_won(int b[3][3], int player) { int i; for(i = 0; i < 3; i++) if(b[i][0] == player && b[i][1] == player && b[i][2] == player) return 1; for(i = 0; i < 3; i++) if(b[0][i] == player && b[1][i] == player && b[2][i] == player) return 1; if(b[0][0] == player && b[1][1] == player && b[2][2] == player) return 1; if(b[0][2] == player && b[1][1] == player && b[2][0] == player) return 1; return 0; }

int game_tree(int b[3][3], int who) { if(has_won(b,1)) return 1; if(has_won(b,2)) return -1; int cells = 0; for(int i = 0; i < 9; i++) if(b[i/3][i%3] == 0) cells++; if(!cells) return 0; int opt = who == 1 ? -9 : 9; for(int i = 0; i < 9; i++) if(b[i/3][i%3] == 0) { b[i/3][i%3] = who; int v = game_tree(b, 3-who); b[i/3][i%3] = 0; if(who == 1 && v > opt) opt = v; if(who == 2 && v < opt) opt = v; } return opt; }

void print_winner(int outcome) { puts(outcome > 0 ? "Takahashi" : outcome < 0 ? "Aoki" : "Draw"); }

void get_board(int a[3][3]) { for(int i = 0; i < 3; i++) for(int j = 0; j < 3; j++) scanf("%d", &a[i][j]); }

int winner(int a[3][3], int p) { for(int i = 0; i < 3; i++) if(a[i][0]==p&&a[i][1]==p&&a[i][2]==p) return 1; for(int j = 0; j < 3; j++) if(a[0][j]==p&&a[1][j]==p&&a[2][j]==p) return 1; return (a[0][0]==p&&a[1][1]==p&&a[2][2]==p) || (a[0][2]==p&&a[1][1]==p&&a[2][0]==p); }

int best_move(int a[3][3], int t) { if(winner(a,1)) return 100; if(winner(a,2)) return -100; int free = 0; for(int i = 0; i < 3; i++) for(int j = 0; j < 3; j++) if(!a[i][j]) free++; if(!free) return 0; int score = t==1 ? -999 : 999; for(int i = 0; i < 3; i++) for(int j = 0; j < 3; j++) if(!a[i][j]) { a[i][j] = t; int s = best_move(a, 3-t); a[i][j] = 0; if(t == 1) score = s > score ? s : score; else score = s < score ? s : score; } return score; }

void print_result(int s) { printf("%s\n", s > 0 ? "Takahashi" : s < 0 ? "Aoki" : "Draw"); }

void scan_board(int m[3][3]) { for(int i = 0; i < 3; i++) for(int j = 0; j < 3; j++) scanf("%d", &m[i][j]); }

int is_winner(int m[3][3], int player) { int w = 0; for(int i = 0; i < 3 && !w; i++) w = (m[i][0]==player&&m[i][1]==player&&m[i][2]==player); for(int j = 0; j < 3 && !w; j++) w = (m[0][j]==player&&m[1][j]==player&&m[2][j]==player); w = w || (m[0][0]==player&&m[1][1]==player&&m[2][2]==player); return w || (m[0][2]==player&&m[1][1]==player&&m[2][0]==player); }

int solve_game(int m[3][3], int p) { if(is_winner(m,1)) return 10; if(is_winner(m,2)) return -10; int moves = 0; for(int k = 0; k < 9; k++) if(m[k/3][k%3]==0) moves++; if(!moves) return 0; int val = p==1 ? -99 : 99; for(int k = 0; k < 9; k++) if(m[k/3][k%3]==0) { m[k/3][k%3] = p; int v = solve_game(m, 3-p); m[k/3][k%3] = 0; val = p==1 ? (v>val?v:val) : (v<val?v:val); } return val; }

void output_winner(int v) { puts(v>0?"Takahashi":v<0?"Aoki":"Draw"); }

void read_matrix(int g[3][3]) { for(int i = 0; i < 9; i++) scanf("%d", &g[i/3][i%3]); }

int check_winner(int g[3][3], int p) { int i, j, w = 0; for(i = 0; i < 3; i++) w |= (g[i][0]==p&&g[i][1]==p&&g[i][2]==p); for(j = 0; j < 3; j++) w |= (g[0][j]==p&&g[1][j]==p&&g[2][j]==p); w |= (g[0][0]==p&&g[1][1]==p&&g[2][2]==p) || (g[0][2]==p&&g[1][1]==p&&g[2][0]==p); return w; }

int alphabeta(int g[3][3], int turn) { if(check_winner(g,1)) return 1; if(check_winner(g,2)) return -1; int empty = 0; for(int i = 0; i < 9; i++) if(g[i/3][i%3]==0) empty++; if(!empty) return 0; int best = turn==1 ? -2 : 2; for(int i = 0; i < 9; i++) if(g[i/3][i%3]==0) { g[i/3][i%3] = turn; int val = alphabeta(g, 3-turn); g[i/3][i%3] = 0; best = turn==1 ? (val>best?val:best) : (val<best?val:best); } return best; }

void print_answer(int r) { printf("%s\n", r>0?"Takahashi":r<0?"Aoki":"Draw"); }
