import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    parts = input().split()
    u, v, c = int(parts[0]), int(parts[1]), parts[2]
    graph[u].append((v, c))

memo = {}

def can_win(max_pos, lucas_pos, last_char, is_max_turn):
    key = (max_pos, lucas_pos, last_char, is_max_turn)
    if key in memo:
        return memo[key]
    
    current_pos = max_pos if is_max_turn else lucas_pos
    
    for next_pos, edge_char in graph[current_pos]:
        if edge_char >= last_char:
            new_max = next_pos if is_max_turn else max_pos
            new_lucas = lucas_pos if is_max_turn else next_pos
            
            if not can_win(new_max, new_lucas, edge_char, not is_max_turn):
                memo[key] = True
                return True
    
    memo[key] = False
    return False

result = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if can_win(i, j, '', True):
            result.append('A')
        else:
            result.append('B')

print(''.join(result))
