n, k, p = map(int, input().split())
arr = list(map(int, input().split()))

odds = []
evens = []
for x in arr:
    if x % 2 == 1:
        odds.append(x)
    else:
        evens.append(x)

odd_count = len(odds)
even_count = len(evens)

# Check conditions
if odd_count < k - p:
    print("NO")
elif (odd_count - (k - p)) % 2 != 0:
    print("NO")
elif p > 0 and odd_count > 2 * n - p - k:
    print("NO")
else:
    print("YES")
    parts = []
    
    # Create k-p parts with 1 odd each
    for i in range(k - p):
        parts.append([odds[i]])
    
    # Remaining
    remaining_odds = odds[k-p:]
    remaining_evens = evens
    
    if p == 0:
        # Add all remaining to the last part
        parts[-1].extend(remaining_odds)
        parts[-1].extend(remaining_evens)
    else:
        # Create p parts with even sum
        # Use evens first for p-1 parts
        used_evens = min(p - 1, even_count)
        for i in range(used_evens):
            parts.append([remaining_evens[i]])
        
        # Use pairs of odds for remaining parts needed
        need_more = (p - 1) - used_evens
        used_odds = 0
        for i in range(need_more):
            parts.append(remaining_odds[used_odds:used_odds+2])
            used_odds += 2
        
        # Last part gets everything else
        remaining = remaining_odds[used_odds:] + remaining_evens[used_evens:]
        parts.append(remaining)
    
    # Output
    for part in parts:
        print(len(part), *part)
