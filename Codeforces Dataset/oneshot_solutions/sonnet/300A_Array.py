n = int(input())
arr = list(map(int, input().split()))

neg = [x for x in arr if x < 0]
pos = [x for x in arr if x > 0]
zero = [x for x in arr if x == 0]

# First set: 1 negative (product < 0)
first = [neg[0]]

# Remaining negatives after taking one for first set
remaining_neg = neg[1:]

# Second set needs even number of negatives for product > 0
if len(remaining_neg) % 2 == 1:
    # Odd remaining: move one to third set
    third = zero + [remaining_neg[0]]
    second = remaining_neg[1:] + pos
else:
    # Even remaining: all go to second set
    third = zero
    second = remaining_neg + pos

# Output
print(len(first), *first)
print(len(second), *second)
print(len(third), *third)
