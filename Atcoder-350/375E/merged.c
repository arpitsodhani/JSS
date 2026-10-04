void add_element_to_window(int pos) {
    int value = array[pos];
    frequency[value]++;
    if (frequency[value] == 1) distinct_count++;
}

void remove_element_from_window(int pos) {
    int value = array[pos];
    frequency[value]--;
    if (frequency[value] == 0) distinct_count--;
}

int compare_mo_queries(const void *a, const void *b) {
    Query *qa = (Query *)a;
    Query *qb = (Query *)b;
    int block_a = qa->left / block_size;
    int block_b = qb->left / block_size;
    if (block_a != block_b) return block_a - block_b;
    return (block_a & 1) ? (qb->right - qa->right) : (qa->right - qb->right);
}

void process_mo_queries(int num_queries) {
    qsort(queries, num_queries, sizeof(Query), compare_mo_queries);
    int current_left = 0, current_right = -1;
    for (int i = 0; i < num_queries; i++) {
        while (current_right < queries[i].right)
            add_element_to_window(++current_right);
        while (current_right > queries[i].right)
            remove_element_from_window(current_right--);
        while (current_left < queries[i].left)
            remove_element_from_window(current_left++);
        while (current_left > queries[i].left)
            add_element_to_window(--current_left);
        answers[queries[i].index] = distinct_count;
    }
}

int main() {
    int n, q;
    scanf("%d %d", &n, &q);
    block_size = (int)sqrt(n) + 1;
    for (int i = 0; i < n; i++)
        scanf("%d", &array[i]);
    for (int i = 0; i < q; i++) {
        scanf("%d %d", &queries[i].left, &queries[i].right);
        queries[i].index = i;
    }
    process_mo_queries(q);
    for (int i = 0; i < q; i++)
        printf("%d\n", answers[i]);
    return 0;
}

