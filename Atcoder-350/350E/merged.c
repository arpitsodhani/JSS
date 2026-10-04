#include <stdlib.h>


void initialize_dp() {
#include <stdio.h>
#include <string.h>
#include <math.h>

long long n, a, x, y;
double memo[1000006];
int visited[1000006];

void initialize_dp() {
    memset(visited, 0, sizeof(visited));
    memo[0] = 0.0;
    visited[0] = 1;
}

double solve_dp(long long k) {
    if (k == 0) return 0.0;
    if (visited[k]) return memo[k];
    
    double choice1 = x + solve_dp(k / a);
    
    double choice2 = y;
    for (int b = 1; b <= 6; b++) {
        choice2 += solve_dp(k / b) / 6.0;
    }
    
    double result = (choice1 < choice2) ? choice1 : choice2;
    memo[k] = result;
    visited[k] = 1;
    return result;
}

double calculate_result() {
    return solve_dp(n);
}

int main() {
    scanf("%lld %lld %lld %lld", &n, &a, &x, &y);
    initialize_dp();
    printf("%.10f\n", calculate_result());
    return 0;
}
}

double solve_dp(long long) {

}

double calculate_result() {

}

int main() {

}

void initialize_dp() {
#include <stdio.h>
#include <string.h>

long long n, a, x, y;
double dp[1000006];
int computed[1000006];

void initialize_dp() {
    for (int i = 0; i <= 1000005; i++) {
        computed[i] = 0;
        dp[i] = 0.0;
    }
    dp[0] = 0.0;
    computed[0] = 1;
}

double get_value(long long k);

double solve_dp(long long k) {
    if (computed[k]) return dp[k];
    
    double opt1 = x + get_value(k / a);
    
    double opt2 = y;
    for (int dice = 1; dice <= 6; dice++) {
        opt2 += get_value(k / dice) / 6.0;
    }
    
    dp[k] = (opt1 < opt2) ? opt1 : opt2;
    computed[k] = 1;
    return dp[k];
}

double get_value(long long k) {
    if (k == 0) return 0.0;
    return solve_dp(k);
}

double calculate_result() {
    return solve_dp(n);
}

int main() {
    scanf("%lld %lld %lld %lld", &n, &a, &x, &y);
    initialize_dp();
    printf("%.10f\n", calculate_result());
    return 0;
}
}

double solve_dp(long long) {

}

double calculate_result() {

}

int main() {

}

void initialize_dp() {
#include <stdio.h>
#include <string.h>

long long n, a, x, y;
double cache[1000006];
int cached[1000006];

void initialize_dp() {
    int i;
    for (i = 0; i <= 1000000; i++) {
        cached[i] = 0;
    }
    cache[0] = 0.0;
    cached[0] = 1;
}

double solve_dp(long long val) {
    if (val == 0) return 0.0;
    if (cached[val]) return cache[val];
    
    double pay_cost = x + solve_dp(val / a);
    
    double roll_dice = y;
    int b;
    for (b = 1; b <= 6; b++) {
        roll_dice += solve_dp(val / b) / 6.0;
    }
    
    double best = pay_cost;
    if (roll_dice < best) best = roll_dice;
    
    cache[val] = best;
    cached[val] = 1;
    return best;
}

double calculate_result() {
    return solve_dp(n);
}

int main() {
    scanf("%lld %lld %lld %lld", &n, &a, &x, &y);
    initialize_dp();
    printf("%.10f\n", calculate_result());
    return 0;
}
}

double solve_dp(long long) {

}

double calculate_result() {

}

int main() {

}

void initialize_dp() {
#include <stdio.h>
#include <string.h>

long long n, a, x, y;
double mem[1000006];
int done[1000006];

void initialize_dp() {
    memset(done, 0, sizeof(done));
    memset(mem, 0, sizeof(mem));
    done[0] = 1;
}

double solve_dp(long long num) {
    if (num == 0) return 0.0;
    if (done[num]) return mem[num];
    
    double path1 = x + solve_dp(num / a);
    double path2 = y;
    
    for (int i = 1; i <= 6; i++) {
        path2 += solve_dp(num / i) / 6.0;
    }
    
    mem[num] = (path1 < path2) ? path1 : path2;
    done[num] = 1;
    return mem[num];
}

double calculate_result() {
    return solve_dp(n);
}

int main() {
    scanf("%lld %lld %lld %lld", &n, &a, &x, &y);
    initialize_dp();
    printf("%.10f\n", calculate_result());
    return 0;
}
}

double solve_dp(long long) {

}

double calculate_result() {

}

int main() {

}

void initialize_dp() {
#include <stdio.h>
#include <string.h>

long long n, a, x, y;
double table[1000006];
int ready[1000006];

void initialize_dp() {
    for (int idx = 0; idx <= 1000000; idx++) {
        ready[idx] = 0;
        table[idx] = 0.0;
    }
    table[0] = 0.0;
    ready[0] = 1;
}

double solve_dp(long long state) {
    if (state == 0) return 0.0;
    if (ready[state]) return table[state];
    
    double action_a = x + solve_dp(state / a);
    double action_b = y;
    
    for (int d = 1; d <= 6; d++) {
        action_b += solve_dp(state / d) / 6.0;
    }
    
    double min_cost = action_a;
    if (action_b < min_cost) min_cost = action_b;
    
    table[state] = min_cost;
    ready[state] = 1;
    return min_cost;
}

double calculate_result() {
    return solve_dp(n);
}

int main() {
    scanf("%lld %lld %lld %lld", &n, &a, &x, &y);
    initialize_dp();
    printf("%.10f\n", calculate_result());
    return 0;
}
}

double solve_dp(long long) {

}

double calculate_result() {

}

int main() {

}
