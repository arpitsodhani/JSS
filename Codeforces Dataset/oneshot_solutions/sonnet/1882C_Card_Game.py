import sys
from functools import lru_cache

def solve(cards):
    n = len(cards)
    
    @lru_cache(maxsize=None)
    def f(remaining):
        if not remaining:
            return 0
        
        arr_len = len(remaining)
        result = 0  # option to end game
        
        # Option 1: Take from odd positions (1, 3, 5, ...)
        for pos in range(1, arr_len + 1, 2):
            idx = pos - 1
            val = cards[remaining[idx]]
            new_remaining = remaining[:idx] + remaining[idx+1:]
            result = max(result, val + f(new_remaining))
        
        # Option 2: Remove from even positions (2, 4, 6, ...)
        for pos in range(2, arr_len + 1, 2):
            idx = pos - 1
            new_remaining = remaining[:idx] + remaining[idx+1:]
            result = max(result, f(new_remaining))
        
        return result
    
    initial = tuple(range(n))
    return f(initial)

def main():
    input_data = sys.stdin.read().strip().split('\n')
    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        n = int(input_data[idx])
        cards = list(map(int, input_data[idx + 1].split()))
        idx += 2
        print(solve(cards))

if __name__ == "__main__":
    main()
