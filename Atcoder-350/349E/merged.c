

long long read_L() { long long L; scanf("%lld", &L); return L; }

int count_pairs(long long L) { int cnt = 0; long long pow = 1; while(pow <= L) { long long l = ((L-1) / pow) * pow; long long r = l + pow; if(l < L && L <= r) cnt++; pow *= 2; } return cnt; }

void print_count(int cnt) { printf("%d\n", cnt); }

void print_pairs(long long L) { long long pow = 1; while(pow <= L) { long long n = (L-1) / pow; long long l = n * pow; long long r = l + pow; if(l < L && L <= r) printf("%lld %lld\n", l, r); pow *= 2; } }

int main() { long long L = read_L(); int cnt = count_pairs(L); print_count(cnt); print_pairs(L); return 0; }

long long input_L() { long long x; scanf("%lld", &x); return x; }

int find_pairs(long long L, long long *pairs) { int idx = 0; for(long long p = 1; p <= L; p <<= 1) { long long l = ((L-1)/p)*p; if(l < L && L <= l+p) { pairs[idx++] = l; pairs[idx++] = l+p; } } return idx/2; }

void output_result(int n, long long *pairs) { printf("%d\n", n); for(int i = 0; i < n; i++) printf("%lld %lld\n", pairs[2*i], pairs[2*i+1]); }

long long get_L() { long long L; scanf("%lld", &L); return L; }

int compute(long long L, long long *res) { int c = 0; long long pow2 = 1; while(pow2 <= L) { long long n = (L-1)/pow2; long long l = n*pow2, r = (n+1)*pow2; if(l < L && L <= r) { res[c*2] = l; res[c*2+1] = r; c++; } pow2 = pow2 * 2; } return c; }

void write_output(int cnt, long long *res) { printf("%d\n", cnt); for(int i = 0; i < cnt; i++) printf("%lld %lld\n", res[2*i], res[2*i+1]); }

long long scan_L() { long long val; scanf("%lld", &val); return val; }

int solve(long long L, long long *ans) { int count = 0; for(long long power = 1; power <= L; power *= 2) { long long left = ((L-1)/power)*power; long long right = left + power; if(left < L && L <= right) { ans[count++] = left; ans[count++] = right; } } return count/2; }

void print_ans(int n, long long *ans) { printf("%d\n", n); for(int i = 0; i < n*2; i += 2) printf("%lld %lld\n", ans[i], ans[i+1]); }

long long read_input() { long long L; scanf("%lld", &L); return L; }

int calculate(long long L, long long *out) { int num = 0; long long bit = 1; do { long long l = ((L-1)/bit)*bit; long long r = l+bit; if(l < L && r >= L) { out[num*2] = l; out[num*2+1] = r; num++; } bit <<= 1; } while(bit <= L); return num; }

void display(int cnt, long long *out) { printf("%d\n", cnt); for(int i = 0; i < cnt; i++) printf("%lld %lld\n", out[i*2], out[i*2+1]); }
