void build_wavelet_node(int node, int left, int right, int *arr, int arr_size) {
    if (left == right) return;
    int mid = (left + right) / 2;
    int left_arr[MAX_N], right_arr[MAX_N];
    int left_count = 0, right_count = 0;
    for (int i = 0; i < arr_size; i++) {
        int bit = (arr[i] <= mid) ? 0 : 1;
        wavelet_bits[node][i] = bit;
        if (i > 0) wavelet_prefix[node][i] = wavelet_prefix[node][i - 1];
        else wavelet_prefix[node][i] = 0;
        if (bit == 0) {
            wavelet_prefix[node][i]++;
            left_arr[left_count++] = arr[i];
        } else {
            right_arr[right_count++] = arr[i];
        }
    }
    build_wavelet_node(2 * node, left, mid, left_arr, left_count);
    build_wavelet_node(2 * node + 1, mid + 1, right, right_arr, right_count);
}

int query_kth_smallest_wavelet(int node, int left, int right, int qleft, int qright, int k) {
    if (left == right) return left;
    int mid = (left + right) / 2;
    int left_count = wavelet_prefix[node][qright];
    if (qleft > 0) left_count -= wavelet_prefix[node][qleft - 1];
    if (k <= left_count) {
        int new_qleft = (qleft > 0) ? wavelet_prefix[node][qleft - 1] : 0;
        int new_qright = wavelet_prefix[node][qright] - 1;
        return query_kth_smallest_wavelet(2 * node, left, mid, new_qleft, new_qright, k);
    } else {
        int new_qleft = qleft - ((qleft > 0) ? wavelet_prefix[node][qleft - 1] : 0);
        int new_qright = qright - wavelet_prefix[node][qright];
        return query_kth_smallest_wavelet(2 * node + 1, mid + 1, right, new_qleft, new_qright, k - left_count);
    }
}

int count_range_less_than(int node, int left, int right, int qleft, int qright, int value) {
    if (left >= value || qleft > qright) return 0;
    if (right < value) return qright - qleft + 1;
    
    int mid = (left + right) / 2;
    int left_count = wavelet_prefix[node][qright];
    if (qleft > 0) left_count -= wavelet_prefix[node][qleft - 1];
    
    int result = 0;
    if (value > mid) {
        result += left_count;
        int new_qleft = qleft - ((qleft > 0) ? wavelet_prefix[node][qleft - 1] : 0);
        int new_qright = qright - wavelet_prefix[node][qright];
        result += count_range_less_than(2 * node + 1, mid + 1, right, new_qleft, new_qright, value);
    } else {
        int new_qleft = (qleft > 0) ? wavelet_prefix[node][qleft - 1] : 0;
        int new_qright = wavelet_prefix[node][qright] - 1;
        result = count_range_less_than(2 * node, left, mid, new_qleft, new_qright, value);
    }
    return result;
}

void initialize_wavelet_arrays(int max_nodes, int max_size) {
    for (int i = 0; i < max_nodes; i++) {
        for (int j = 0; j < max_size; j++) {
            wavelet_bits[i][j] = 0;
            wavelet_prefix[i][j] = 0;
        }
    }
}

int main() {
    int n, q;
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n; i++)
        scanf("%d", &array[i]);
    build_wavelet_node(1, 0, MAX_VAL, array, n);
    for (int i = 0; i < q; i++) {
        int left, right, k;
        scanf("%d %d %d", &left, &right, &k);
        printf("%d\n", query_kth_smallest_wavelet(1, 0, MAX_VAL, left, right, k));
    }
    return 0;
}

