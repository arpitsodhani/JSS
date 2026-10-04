

int read_n() { int n; scanf("%d", &n); return n; }

int sum_scores(int count) { int sum = 0; for(int i = 0; i < count; i++) { int x; scanf("%d", &x); sum += x; } return sum; }

int compute(int s) { return -s; }

void output(int ans) { printf("%d\n", ans); }

int main() { int n = read_n(); int sum = sum_scores(n-1); int ans = compute(sum); output(ans); return 0; }

int get_input(int *arr, int n) { int count; scanf("%d", &count); for(int i = 0; i < count-1; i++) scanf("%d", &arr[i]); return count-1; }

int calculate(int *arr, int len) { int total = 0; int i = 0; while(i < len) { total += arr[i++]; } return -total; }

void print_res(int result) { printf("%d\n", result); }

int accumulate() { int n, sum = 0; scanf("%d", &n); for(int j = 1; j < n; j++) { int val; scanf("%d", &val); sum = sum + val; } return sum; }

int negate(int x) { return 0 - x; }

void display(int res) { printf("%d\n", res); }

int read_rec(int rem) { if(rem == 0) return 0; int v; scanf("%d", &v); return v + read_rec(rem-1); }

int invert(int num) { return -num; }

void write(int a) { printf("%d\n", a); }

int fast_sum(int cnt) { int s = 0, i = cnt; while(i--) { int x; scanf("%d", &x); s += x; } return s; }

int flip(int v) { return (~v) + 1; }

void out(int r) { printf("%d\n", r); }
