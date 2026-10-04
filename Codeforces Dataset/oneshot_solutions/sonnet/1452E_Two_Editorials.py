import sys

def main():
    input_data = sys.stdin.read().split()
    
    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])
    
    participants = []
    idx = 3
    for i in range(m):
        l = int(input_data[idx])
        r = int(input_data[idx + 1])
        participants.append((l, r))
        idx += 2
    
    def overlap(l, r, s):
        return max(0, min(r, s + k - 1) - max(l, s) + 1)
    
    max_sum = 0
    
    for s1 in range(1, n - k + 2):
        overlaps_s1 = [overlap(l, r, s1) for l, r in participants]
        for s2 in range(1, n - k + 2):
            total = 0
            for i in range(m):
                l, r = participants[i]
                total += max(overlaps_s1[i], overlap(l, r, s2))
            max_sum = max(max_sum, total)
    
    print(max_sum)

if __name__ == "__main__":
    main()
