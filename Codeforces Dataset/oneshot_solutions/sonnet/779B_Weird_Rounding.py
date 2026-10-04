n, k = input().split()
k = int(k)

zero_count = n.count('0')

# If not enough zeros, result must be "0"
if zero_count < k:
    print(len(n) - 1)
# If all zeros, result is "0"
elif all(d == '0' for d in n):
    print(len(n) - 1)
else:
    # Find first non-zero digit
    first_nonzero_idx = -1
    for i, digit in enumerate(n):
        if digit != '0':
            first_nonzero_idx = i
            break
    
    # Find all zero positions after first non-zero
    zero_positions = []
    for i in range(first_nonzero_idx + 1, len(n)):
        if n[i] == '0':
            zero_positions.append(i)
    
    # If not enough zeros after first non-zero, result must be "0"
    if len(zero_positions) < k:
        print(len(n) - 1)
    else:
        # Keep first non-zero, all digits up to the first of the last k zeros,
        # and the last k zeros
        first_of_last_k_zeros = zero_positions[-k]
        
        # Number of kept digits:
        # 1 (first non-zero) + digits between + k (last k zeros)
        kept = 1 + (first_of_last_k_zeros - first_nonzero_idx - 1) + k
        
        print(len(n) - kept)
