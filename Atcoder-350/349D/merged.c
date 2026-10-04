

void read_input(int *n, int *k, long long *arr) { scanf("%d%d", n, k); for(int i = 0; i < *n; i++) scanf("%lld", &arr[i]); }

void sort_desc(long long *arr, int n) { for(int i = 0; i < n-1; i++) for(int j = i+1; j < n; j++) if(arr[i] < arr[j]) { long long tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp; } }

long long compute_sum(long long *arr, int k) { long long sum = 0; for(int i = 0; i < k; i++) sum += arr[i]; return sum; }

void output(long long ans) { printf("%lld\n", ans); }

int main() { int n, k; long long arr[200001]; read_input(&n, &k, arr); sort_desc(arr, n); output(compute_sum(arr, k)); return 0; }

int input_data(int *k, long long *a) { int n; scanf("%d%d", &n, k); for(int i = 0; i < n; i++) scanf("%lld", &a[i]); return n; }

void bubble_sort(long long *a, int n) { int swapped = 1; while(swapped) { swapped = 0; for(int i = 0; i < n-1; i++) if(a[i] < a[i+1]) { long long t = a[i]; a[i] = a[i+1]; a[i+1] = t; swapped = 1; } } }

long long sum_top_k(long long *a, int k) { long long s = 0; int i = 0; while(i < k) { s += a[i]; i++; } return s; }

void print_result(long long r) { printf("%lld\n", r); }

int get_input(int *k, long long *vals) { int n; scanf("%d%d", &n, k); for(int i = 0; i < n; i++) scanf("%lld", vals+i); return n; }

void selection_sort(long long *v, int n) { for(int i = 0; i < n-1; i++) { int maxIdx = i; for(int j = i+1; j < n; j++) if(v[j] > v[maxIdx]) maxIdx = j; long long tmp = v[i]; v[i] = v[maxIdx]; v[maxIdx] = tmp; } }

long long calc_sum(long long *v, int cnt) { long long total = 0; for(int j = 0; j < cnt; j++) total += v[j]; return total; }

void write_ans(long long ans) { printf("%lld\n", ans); }

int scan_values(int *k, long long *arr) { int n; scanf("%d%d", &n, k); for(int i = 0; i < n; i++) scanf("%lld", &arr[i]); return n; }

void insertion_sort(long long *arr, int n) { for(int i = 1; i < n; i++) { long long key = arr[i]; int j = i-1; while(j >= 0 && arr[j] < key) { arr[j+1] = arr[j]; j--; } arr[j+1] = key; } }

long long sum_first_k(long long *arr, int k) { long long sum = 0; for(int i = 0; i < k; sum += arr[i], i++); return sum; }

void output_ans(long long a) { printf("%lld\n", a); }

int read_data(int *keep, long long *nums) { int n; scanf("%d%d", &n, keep); for(int i = 0; i < n; i++) scanf("%lld", &nums[i]); return n; }

void qsort_desc(long long *a, int n) { if(n <= 1) return; long long pivot = a[n/2]; int i = 0, j = n-1; while(i <= j) { while(a[i] > pivot) i++; while(a[j] < pivot) j--; if(i <= j) { long long t = a[i]; a[i] = a[j]; a[j] = t; i++; j--; } } if(j > 0) qsort_desc(a, j+1); if(i < n) qsort_desc(a+i, n-i); }

long long accumulate(long long *a, int k) { long long acc = 0; for(int i = 0; i < k; i++) acc = acc + a[i]; return acc; }

void print_ans(long long res) { printf("%lld\n", res); }
