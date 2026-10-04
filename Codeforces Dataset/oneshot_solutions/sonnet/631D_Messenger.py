import sys

def parse_block(token):
    length, char = token.split('-')
    return (int(length), char)

def merge_blocks(blocks):
    merged = []
    for length, char in blocks:
        if merged and merged[-1][1] == char:
            merged[-1] = (merged[-1][0] + length, char)
        else:
            merged.append((length, char))
    return merged

def build_prefix(pattern):
    prefix = [0] * len(pattern)
    j = 0
    
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix[i] = j
    
    return prefix

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    
    text = []
    for _ in range(n):
        text.append(parse_block(data[idx]))
        idx += 1
    
    pattern = []
    for _ in range(m):
        pattern.append(parse_block(data[idx]))
        idx += 1
    
    text = merge_blocks(text)
    pattern = merge_blocks(pattern)
    
    n = len(text)
    m = len(pattern)
    
    if m == 1:
        need_len, need_char = pattern[0]
        answer = 0
        for length, char in text:
            if char == need_char and length >= need_len:
                answer += length - need_len + 1
        print(answer)
        return
    
    if m == 2:
        first_len, first_char = pattern[0]
        second_len, second_char = pattern[1]
        answer = 0
        
        for i in range(n - 1):
            if (text[i][1] == first_char and text[i][0] >= first_len and
                text[i + 1][1] == second_char and text[i + 1][0] >= second_len):
                answer += 1
        
        print(answer)
        return
    
    middle = pattern[1:-1]
    prefix = build_prefix(middle)
    first_len, first_char = pattern[0]
    last_len, last_char = pattern[-1]
    
    answer = 0
    j = 0
    
    for i in range(n):
        while j > 0 and text[i] != middle[j]:
            j = prefix[j - 1]
        
        if text[i] == middle[j]:
            j += 1
        
        if j == len(middle):
            start = i - len(middle) + 1
            
            if start > 0 and i + 1 < n:
                left_len, left_char = text[start - 1]
                right_len, right_char = text[i + 1]
                
                if (left_char == first_char and left_len >= first_len and
                    right_char == last_char and right_len >= last_len):
                    answer += 1
            
            j = prefix[j - 1]
    
    print(answer)

if __name__ == "__main__":
    main()
