from collections import deque, Counter

n = int(input())
cards = list(map(int, input().split()))

deck = deque(cards)
counter = Counter(cards)
count = 0

while deck:
    min_val = min(counter)
    num_to_remove = counter[min_val]
    removed = 0
    
    while removed < num_to_remove:
        count += 1
        if deck[0] == min_val:
            deck.popleft()
            removed += 1
        else:
            deck.append(deck.popleft())
    
    del counter[min_val]

print(count)
