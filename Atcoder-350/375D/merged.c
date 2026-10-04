void build_sqrt_layer(int *arr, int n, int layer) {
    int block_size = (int)sqrt(n) + 1;
    for (int i = 0; i < n; i += block_size) {
        long long block_sum = 0;
        for (int j = i; j < n && j < i + block_size; j++) {
            block_sum += arr[j];
        }
        sqrt_blocks[layer][i / block_size] = block_sum;
    }
}

void update_sqrt_tree_point(int pos, long long delta) {
    array[pos] += delta;
    int block_size = (int)sqrt(n) + 1;
    int block_id = pos / block_size;
    sqrt_blocks[0][block_id] += delta;
    for (int layer = 1; layer < num_layers; layer++) {
        int upper_block_size = (int)sqrt(block_size) + 1;
        int upper_block_id = block_id / upper_block_size;
        sqrt_blocks[layer][upper_block_id] += delta;
        block_id = upper_block_id;
        block_size = upper_block_size;
    }
}

long long query_sqrt_tree_range(int left, int right) {
    long long result = 0;
    int block_size = (int)sqrt(n) + 1;
    int left_block = left / block_size;
    int right_block = right / block_size;
    if (left_block == right_block) {
        for (int i = left; i <= right; i++)
            result += array[i];
    } else {
        for (int i = left; i < (left_block + 1) * block_size; i++)
            result += array[i];
        for (int b = left_block + 1; b < right_block; b++)
            result += sqrt_blocks[0][b];
        for (int i = right_block * block_size; i <= right; i++)
            result += array[i];
    }
    return result;
}

int compute_block_size(int n) {
    int size = 1;
    while (size * size < n) size++;
    return size;
}

int main() {
    int q;
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n; i++)
        scanf("%lld", &array[i]);
    build_sqrt_layer(array, n, 0);
    for (int i = 0; i < q; i++) {
        int type;
        scanf("%d", &type);
        if (type == 1) {
            int pos; long long delta;
            scanf("%d %lld", &pos, &delta);
            update_sqrt_tree_point(pos, delta);
        } else {
            int left, right;
            scanf("%d %d", &left, &right);
            printf("%lld\n", query_sqrt_tree_range(left, right));
        }
    }
    return 0;
}

