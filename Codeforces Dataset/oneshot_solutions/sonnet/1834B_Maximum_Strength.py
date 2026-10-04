def solve():
    l, r = map(int, input().split())
    
    l_str = str(l)
    r_str = str(r)
    
    # Pad to same length
    max_len = max(len(l_str), len(r_str))
    l_str = l_str.zfill(max_len)
    r_str = r_str.zfill(max_len)
    
    # Find first differing position
    diff_pos = -1
    for i in range(max_len):
        if l_str[i] != r_str[i]:
            diff_pos = i
            break
    
    if diff_pos == -1:
        return 0
    
    # After first diff, we can maximize with 9s and 0s
    remaining = max_len - diff_pos - 1
    return int(r_str[diff_pos]) - int(l_str[diff_pos]) + 9 * remaining

t = int(input())
for _ in range(t):
    print(solve())
