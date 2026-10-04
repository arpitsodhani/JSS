int build_cartesian_tree(int *arr, int n) {
    int stack[MAX_N], top = -1;
    for (int i = 0; i < n; i++) {
        cartesian_left[i] = cartesian_right[i] = -1;
        int last_popped = -1;
        while (top >= 0 && arr[stack[top]] > arr[i]) {
            last_popped = stack[top--];
        }
        if (last_popped != -1)
            cartesian_left[i] = last_popped;
        if (top >= 0)
            cartesian_right[stack[top]] = i;
        stack[++top] = i;
    }
    return stack[0];
}

void compute_cartesian_depth(int node, int depth) {
    if (node == -1) return;
    cartesian_depth[node] = depth;
    compute_cartesian_depth(cartesian_left[node], depth + 1);
    compute_cartesian_depth(cartesian_right[node], depth + 1);
}

int find_range_min_cartesian(int left, int right) {
    int min_pos = left;
    for (int i = left; i <= right; i++) {
        if (array[i] < array[min_pos])
            min_pos = i;
    }
    return min_pos;
}

int verify_cartesian_property(int node, int *arr) {
    if (node == -1) return 1;
    
    if (cartesian_left[node] != -1 && arr[cartesian_left[node]] < arr[node])
        return 0;
    if (cartesian_right[node] != -1 && arr[cartesian_right[node]] < arr[node])
        return 0;
    
    return verify_cartesian_property(cartesian_left[node], arr) && 
           verify_cartesian_property(cartesian_right[node], arr);
}

int main() {
    int n, q;
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n; i++)
        scanf("%d", &array[i]);
    int root = build_cartesian_tree(array, n);
    compute_cartesian_depth(root, 0);
    for (int i = 0; i < q; i++) {
        int left, right;
        scanf("%d %d", &left, &right);
        printf("%d\n", array[find_range_min_cartesian(left, right)]);
    }
    return 0;
}

