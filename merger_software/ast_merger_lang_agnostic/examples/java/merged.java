/* Clause C1 [Confidence: 1.00] */
if (a == null || n <= 0) {
    return -1;
}

/* Clause C2 [Confidence: 1.00] */
int max_val = a[0];
int last_idx = 0;
for (int i = 1; i < n; i++) {
    if (a[i] >= max_val) {
        max_val = a[i];
        last_idx = i;
    }
}
return last_idx;

