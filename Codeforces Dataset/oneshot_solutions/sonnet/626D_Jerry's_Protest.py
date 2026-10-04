import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    balls = data[1:]
    
    max_value = max(balls)
    present = [0] * (max_value + 1)
    for x in balls:
        present[x] = 1
    
    diff_count = [0] * (max_value + 1)
    for d in range(1, max_value + 1):
        count = 0
        for x in range(0, max_value - d + 1):
            if present[x] and present[x + d]:
                count += 1
        diff_count[d] = count
    
    pair_sums = [0] * (2 * max_value + 1)
    for i in range(1, max_value + 1):
        if diff_count[i] == 0:
            continue
        ci = diff_count[i]
        for j in range(1, max_value + 1):
            if diff_count[j]:
                pair_sums[i + j] += ci * diff_count[j]
    
    suffix = [0] * (max_value + 2)
    for d in range(max_value, 0, -1):
        suffix[d] = suffix[d + 1] + diff_count[d]
    
    good = 0
    for s in range(2, 2 * max_value + 1):
        if pair_sums[s] and s + 1 <= max_value:
            good += pair_sums[s] * suffix[s + 1]
    
    total_pairs = n * (n - 1) // 2
    total = total_pairs ** 3
    
    print("{:.10f}".format(good / total))

if __name__ == "__main__":
    main()
