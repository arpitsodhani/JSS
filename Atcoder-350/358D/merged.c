#include <stdio.h>
#include <stdlib.h>

void read_arrays(int n, int m, int boxes[], int people[]) { for(int i = 0; i < n; i++) scanf("%d", &boxes[i]); for(int i = 0; i < m; i++) scanf("%d", &people[i]); }

int compare_int(const void *a, const void *b) { return (*(int*)a - *(int*)b); }

void sort_arrays(int n, int m, int boxes[], int people[]) { qsort(boxes, n, sizeof(int), compare_int); qsort(people, m, sizeof(int), compare_int); }

long long match_boxes_to_people(int n, int m, int boxes[], int people[]) { int box_idx = 0, person_idx = 0; long long total = 0; while(person_idx < m) { if(box_idx >= n) return -1; if(boxes[box_idx] >= people[person_idx]) { total += boxes[box_idx]; person_idx++; } box_idx++; } return total; }

int main() { int n, m; scanf("%d%d", &n, &m); int boxes[200005], people[200005]; read_arrays(n, m, boxes, people); sort_arrays(n, m, boxes, people); long long result = match_boxes_to_people(n, m, boxes, people); printf("%lld\n", result); return 0; }
