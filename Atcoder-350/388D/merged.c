

void read_input(int *n, int **arr) {
    scanf("%d", n);
    *arr = malloc(*n * sizeof(int));
    for (int i = 0; i < *n; i++) {
        scanf("%d", &(*arr)[i]);
    }
}

long long compute_sum(int *arr, int n) {
    long long sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return sum;
}

void print_result(long long result) {
    printf("%lld\n", result);
}

int main() {
    int n;
    int *arr;
    read_input(&n, &arr);
    long long result = compute_sum(arr, n);
    print_result(result);
    free(arr);
    return 0;
}
