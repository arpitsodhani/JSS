import sys

def solve(n, c):
    # dp[i][j] = max balls kept from positions 0 to i, using exactly j segments, ball i is kept
    # c is 0-indexed
    max_segments = n
    dp = [[-1] * (max_segments + 1) for _ in range(n)]

    for i in range(n):
        # Start first segment at position i
        dp[i][1] = 1
        # Extend from previous position if increasing
        if i > 0 and dp[i-1][1] >= 0 and c[i-1] < c[i]:
            dp[i][1] = max(dp[i][1], dp[i-1][1] + 1)

        # For j >= 2 segments
        for j in range(2, min(i + 1, max_segments) + 1):
            # Extend j-th segment from position i-1
            if i > 0 and dp[i-1][j] >= 0 and c[i-1] < c[i]:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + 1)

            # Start new j-th segment at position i
            for p in range(i - 1):
                if dp[p][j-1] >= 0 and c[p] < c[i]:
                    dp[i][j] = max(dp[i][j], dp[p][j-1] + 1)

    # Compute max kept for each number of segments
    max_kept_by_segs = [0] * (max_segments + 1)
    for i in range(n):
        for j in range(1, max_segments + 1):
            if dp[i][j] >= 0:
                max_kept_by_segs[j] = max(max_kept_by_segs[j], dp[i][j])

    # Results for k=0 to k=n-1
    results = []
    max_so_far = 0
    for k in range(n):
        # With k color-0 balls, we can have at most k+1 segments
        num_segs = k + 1
        if num_segs <= max_segments:
            max_so_far = max(max_so_far, max_kept_by_segs[num_segs])
        results.append(n - max_so_far)

    return results

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1

    for _ in range(t):
        n = int(input_data[idx])
        k = int(input_data[idx + 1])
        idx += 2
        c = [int(input_data[idx + i]) for i in range(n)]
        idx += n

        results = solve(n, c)
        print(' '.join(map(str, results)))

if __name__ == '__main__':
    main()
