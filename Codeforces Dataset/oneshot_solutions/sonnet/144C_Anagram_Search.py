import sys
from collections import Counter

def solve():
    lines = sys.stdin.read().strip().split('\n')
    s = lines[0]
    p = lines[1]
    
    p_len = len(p)
    p_freq = Counter(p)
    
    if p_len > len(s):
        print(0)
        return
    
    count = 0
    window_freq = Counter()
    
    # Initialize the first window
    for i in range(p_len):
        if s[i] != '?':
            window_freq[s[i]] += 1
    
    # Check if the window is good
    def is_good():
        for ch, cnt in window_freq.items():
            if ch not in p_freq or cnt > p_freq[ch]:
                return False
        return True
    
    if is_good():
        count += 1
    
    # Slide the window
    for i in range(p_len, len(s)):
        # Remove the leftmost character
        if s[i - p_len] != '?':
            ch = s[i - p_len]
            window_freq[ch] -= 1
            if window_freq[ch] == 0:
                del window_freq[ch]
        
        # Add the rightmost character
        if s[i] != '?':
            window_freq[s[i]] += 1
        
        # Check if the current window is good
        if is_good():
            count += 1
    
    print(count)

solve()
