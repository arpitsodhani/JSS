import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx])
    idx += 1
    words = []
    for _ in range(n):
        words.append(input_data[idx])
        idx += 1
    
    # Precompute for each word
    word_data = []
    for word in words:
        counts = [0] * 26
        for c in word:
            counts[ord(c) - ord('a')] += 1
        
        odd_mask = 0
        present_mask = 0
        for i in range(26):
            if counts[i] > 0:
                present_mask |= (1 << i)
                if counts[i] % 2 == 1:
                    odd_mask |= (1 << i)
        
        len_parity = len(word) % 2
        word_data.append((odd_mask, present_mask, len_parity))
    
    full_mask = (1 << 26) - 1
    result = 0
    
    # For each possible missing letter
    for m in range(26):
        target_mask = full_mask ^ (1 << m)
        
        # Count pairs with different length parities
        groups = [defaultdict(int), defaultdict(int)]
        
        for odd_mask, present_mask, len_parity in word_data:
            if present_mask & (1 << m):
                continue  # word contains the missing letter
            groups[len_parity][(odd_mask, present_mask)] += 1
        
        # Count pairs
        for (odd1, pres1), count1 in groups[0].items():
            for (odd2, pres2), count2 in groups[1].items():
                if (pres1 | pres2) == target_mask and (odd1 ^ odd2) == target_mask:
                    result += count1 * count2
    
    print(result)

solve()
