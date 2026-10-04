

int read_input(int *a) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) scanf("%d", &a[i]); return n; }

int solve(int n, int *a, int *ops) { int cnt = 0; for(int i = 0; i < n; i++) { if(a[i] != i+1) { int j = i; while(a[j] != i+1) j++; ops[cnt*2] = i; ops[cnt*2+1] = j; int tmp = a[i]; a[i] = a[j]; a[j] = tmp; cnt++; } } return cnt; }

void output(int cnt, int *ops) { printf("%d\n", cnt); for(int i = 0; i < cnt; i++) printf("%d %d\n", ops[2*i]+1, ops[2*i+1]+1); }

int main() { int a[200001], ops[400002]; int n = read_input(a); int cnt = solve(n, a, ops); output(cnt, ops); return 0; }

int input_array(int *arr) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) scanf("%d", &arr[i]); return n; }

int selection_sort(int n, int *arr, int *swaps) { int moves = 0; for(int i = 0; i < n; i++) { if(arr[i] == i+1) continue; int pos = i; for(int j = i+1; j < n; j++) if(arr[j] == i+1) { pos = j; break; } swaps[moves*2] = i; swaps[moves*2+1] = pos; int t = arr[i]; arr[i] = arr[pos]; arr[pos] = t; moves++; } return moves; }

void print_swaps(int cnt, int *swaps) { printf("%d\n", cnt); for(int i = 0; i < cnt; i++) printf("%d %d\n", swaps[2*i]+1, swaps[2*i+1]+1); }

int get_perm(int *p) { int n; scanf("%d", &n); for(int i = 1; i <= n; i++) scanf("%d", &p[i]); return n; }

int fix_permutation(int n, int *p, int *result) { int count = 0; for(int i = 1; i <= n; i++) { if(p[i] != i) { int where = i; for(int j = i+1; j <= n; j++) if(p[j] == i) { where = j; break; } result[count*2] = i; result[count*2+1] = where; int swap = p[i]; p[i] = p[where]; p[where] = swap; count++; } } return count; }

void write_operations(int num, int *result) { printf("%d\n", num); for(int k = 0; k < num; k++) printf("%d %d\n", result[2*k], result[2*k+1]); }

int scan_perm(int *a) { int n; scanf("%d", &n); for(int i = 1; i <= n; i++) scanf("%d", a+i); return n; }

int sort_perm(int n, int *a, int *moves) { int m = 0; for(int target = 1; target <= n; target++) { if(a[target] == target) continue; int location = target; while(a[location] != target) location++; moves[m++] = target; moves[m++] = location; int temp = a[target]; a[target] = a[location]; a[location] = temp; } return m/2; }

void output_moves(int count, int *moves) { printf("%d\n", count); for(int i = 0; i < count*2; i += 2) printf("%d %d\n", moves[i], moves[i+1]); }

int read_permutation(int *arr) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) scanf("%d", &arr[i]); return n; }

int find_swaps(int n, int *arr, int *log) { int ops = 0; for(int i = 0; i < n; i++) { while(arr[i] != i+1) { int target = arr[i] - 1; log[ops*2] = i; log[ops*2+1] = target; int tmp = arr[i]; arr[i] = arr[target]; arr[target] = tmp; ops++; } } return ops; }

void display_result(int ops, int *log) { printf("%d\n", ops); for(int i = 0; i < ops; i++) printf("%d %d\n", log[i*2]+1, log[i*2+1]+1); }
