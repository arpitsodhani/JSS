# CLAUSE: initialize_reachable_segments
import sys

def reset(m):
    return [(m, m)]

# CLAUSE: split_by_selected_position
def scan_segments(active, a):
    buckets = {"left": [], "right": []}
    hit = 0
    for l, r in active:
        if r < a:
            buckets["left"].append((l, r))
        elif l > a:
            buckets["right"].append((l, r))
        else:
            if l < a:
                buckets["left"].append((l, a - 1))
            hit = 1
            if a < r:
                buckets["right"].append((a + 1, r))
    return buckets, hit

# CLAUSE: propagate_left_side_positions
def push_left_bucket(bucket, n, target):
    for l, r in bucket:
        target.append((l, r + 1 if r < n else n))

# CLAUSE: propagate_right_side_positions
def push_right_bucket(bucket, target):
    for l, r in bucket:
        target.append((l - 1 if l > 1 else 1, r))

# CLAUSE: handle_joker_card_hit
def push_hit(hit, n, target):
    if hit:
        target.append((1, 1))
        target.append((n, n))

# CLAUSE: merge_adjacent_intervals
def merge_all(target):
    target.sort()
    ans = []
    for item in target:
        l, r = item
        if len(ans) == 0 or ans[-1][1] + 1 < l:
            ans.append(item)
        elif ans[-1][1] < r:
            ans[-1] = (ans[-1][0], r)
    return ans

# CLAUSE: count_union_positions
def count_all(active):
    total = 0
    for l, r in active:
        total += r - l + 1
    return total

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = nums[idx]
    idx += 1
    output = []
    for _ in range(t):
        n = nums[idx]
        m = nums[idx + 1]
        q = nums[idx + 2]
        idx += 3
        active = reset(m)
        line = []
        for j in range(q):
            a = nums[idx + j]
            buckets, hit = scan_segments(active, a)
            nxt = []
            push_left_bucket(buckets["left"], n, nxt)
            push_right_bucket(buckets["right"], nxt)
            push_hit(hit, n, nxt)
            active = merge_all(nxt)
            line.append(str(count_all(active)))
        idx += q
        output.append(" ".join(line))
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
