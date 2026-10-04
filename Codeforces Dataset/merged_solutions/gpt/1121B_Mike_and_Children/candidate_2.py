import sys

# CLAUSE: enumerate_pair_sums
def enumerate_pair_sums(a):
    n = len(a)
    return [(a[i] + a[j], (i, j)) for i in range(n) for j in range(i + 1, n)]

# CLAUSE: group_pairs_by_sum
def group_pairs_by_sum(pair_sums):
    pair_sums.sort(key=lambda item: item[0])
    grouped = []
    pos = 0
    while pos < len(pair_sums):
        total = pair_sums[pos][0]
        bucket = []
        while pos < len(pair_sums) and pair_sums[pos][0] == total:
            bucket.append(pair_sums[pos][1])
            pos += 1
        grouped.append(bucket)
    return grouped

# CLAUSE: select_candidate_sum
def select_candidate_sum(grouped):
    for bucket in grouped:
        yield bucket

# CLAUSE: track_used_sweets
def track_used_sweets(size):
    return bytearray(size)

# CLAUSE: count_disjoint_pairs
def count_disjoint_pairs(bucket, size):
    used = track_used_sweets(size)
    total = 0
    for left, right in bucket:
        if used[left] == 0 and used[right] == 0:
            used[left] = 1
            used[right] = 1
            total += 1
    return total

# CLAUSE: maximize_children_count
def maximize_children_count(a):
    grouped = group_pairs_by_sum(enumerate_pair_sums(a))
    answer = 0
    for bucket in select_candidate_sum(grouped):
        current = count_disjoint_pairs(bucket, len(a))
        if current > answer:
            answer = current
    return answer

def main():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    a = [int(x) for x in tokens[1:n + 1]]
    sys.stdout.write(str(maximize_children_count(a)))

main()
