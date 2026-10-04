import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        
        total_zeros = a.count(0)
        ones_before = 0
        zeros_seen = 0
        inversions = 0
        best_gain = 0
        
        for x in a:
            if x == 1:
                ones_before += 1
            else:
                inversions += ones_before
        
        ones_before = 0
        zeros_seen = 0
        
        for x in a:
            zeros_after = total_zeros - zeros_seen - (1 if x == 0 else 0)
            
            if x == 0:
                gain = zeros_after - ones_before
                best_gain = max(best_gain, gain)
                zeros_seen += 1
            else:
                gain = ones_before - zeros_after
                best_gain = max(best_gain, gain)
                ones_before += 1
        
        answers.append(str(inversions + best_gain))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
