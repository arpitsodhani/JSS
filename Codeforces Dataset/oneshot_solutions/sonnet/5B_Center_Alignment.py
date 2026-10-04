import sys

lines = sys.stdin.read().rstrip('\n').split('\n')

max_len = max(len(line) for line in lines)

# Print top border
print('*' * (max_len + 3))

# Print centered lines
odd_count = 0
for line in lines:
    width = max_len + 1
    padding = width - len(line)
    left = padding // 2
    right = padding - left
    
    # Alternate extra space for odd padding
    if padding % 2 == 1:
        if odd_count % 2 == 1:
            left, right = right, left
        odd_count += 1
    
    print('*' + ' ' * left + line + ' ' * right + '*')

# Print bottom border
print('*' * (max_len + 3))
