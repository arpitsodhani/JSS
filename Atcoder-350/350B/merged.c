

void read_input(int *n, int *q, int *t) { scanf("%d%d", n, q); for(int i = 0; i < *q; i++) scanf("%d", &t[i]); }

int process(int n, int q, int *t) { int teeth[1001] = {0}; for(int i = 1; i <= n; i++) teeth[i] = 1; for(int i = 0; i < q; i++) teeth[t[i]] = 1 - teeth[t[i]]; int cnt = 0; for(int i = 1; i <= n; i++) cnt += teeth[i]; return cnt; }

void output(int ans) { printf("%d\n", ans); }

int main() { int n, q, t[1001]; read_input(&n, &q, t); output(process(n, q, t)); return 0; }

int input_data(int *q, int *ops) { int n; scanf("%d%d", &n, q); for(int i = 0; i < *q; i++) scanf("%d", &ops[i]); return n; }

int simulate(int n, int q, int *ops) { int state[1001]; for(int i = 1; i <= n; i++) state[i] = 1; for(int i = 0; i < q; i++) state[ops[i]] ^= 1; int sum = 0; for(int i = 1; i <= n; i++) sum += state[i]; return sum; }

void print_ans(int a) { printf("%d\n", a); }

void get_input(int *n, int *q, int *arr) { scanf("%d%d", n, q); for(int i = 0; i < *q; i++) scanf("%d", arr+i); }

int count_teeth(int n, int q, int *arr) { int has[1001] = {0}; for(int i = 1; i <= n; i++) has[i] = 1; for(int j = 0; j < q; j++) has[arr[j]] = !has[arr[j]]; int total = 0; for(int i = 1; i <= n; i++) if(has[i]) total++; return total; }

void write_output(int res) { printf("%d\n", res); }

void scan_data(int *n, int *q, int *t) { scanf("%d%d", n, q); for(int i = 0; i < *q; i++) scanf("%d", t+i); }

int apply_treatments(int n, int q, int *t) { int present[1001]; for(int k = 1; k <= n; k++) present[k] = 1; for(int k = 0; k < q; k++) present[t[k]] = 1 - present[t[k]]; int count = 0; for(int k = 1; k <= n; k++) count += present[k]; return count; }

void output_count(int c) { printf("%d\n", c); }

void read_nq(int *n, int *q, int *arr) { scanf("%d%d", n, q); for(int i = 0; i < *q; i++) scanf("%d", &arr[i]); }

int toggle_and_count(int n, int q, int *arr) { int bit[1001]; for(int i = 1; i <= n; i++) bit[i] = 1; for(int i = 0; i < q; i++) { int pos = arr[i]; bit[pos] = bit[pos] ? 0 : 1; } int ans = 0; for(int i = 1; i <= n; i++) ans += bit[i]; return ans; }

void print_result(int r) { printf("%d\n", r); }
