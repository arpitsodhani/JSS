# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    trucks = []
    idx = 1
    
    for i in range(1, n + 1):
        v = data[idx]
        c = data[idx + 1]
        l = data[idx + 2]
        r = data[idx + 3]
        idx += 4
        trucks.append((v, c, l, r, i))
    
    max_people = sum(c for _, c, _, _, _ in trucks)
    
    prev_node = [-1]
    node_item = [0]
    
    buckets = {0: [(0, 0, 0)]}  # people -> list of (needed_total, value, node)
    
    def prune(states):
        states.sort(key=lambda x: (x[0], -x[1]))
        result = []
        best_value = -1
        
        for need, value, node in states:
            if value > best_value:
                result.append((need, value, node))
                best_value = value
        
        return result
    
    for v, c, l, r, truck_id in trucks:
        people_keys = sorted(buckets.keys(), reverse=True)
        changed = set()
        
        for people in people_keys:
            if people < l:
                continue
            
            states = buckets[people]
            new_people = people + c
            if new_people > max_people:
                continue
            
            target = buckets.setdefault(new_people, [])
            
            for need, value, node in states:
                new_need = max(need, new_people + r)
                if new_need > max_people:
                    continue
                
                prev_node.append(node)
                node_item.append(truck_id)
                new_node = len(prev_node) - 1
                
                target.append((new_need, value + v, new_node))
                changed.add(new_people)
        
        for people in changed:
            buckets[people] = prune(buckets[people])
    
    best_value = -1
    best_node = 0
    
    for people, states in buckets.items():
        for need, value, node in states:
            if need <= people and value > best_value:
                best_value = value
                best_node = node
    
    answer = []
    while best_node != 0:
        answer.append(node_item[best_node])
        best_node = prev_node[best_node]
    
    answer.reverse()
    
    print(len(answer))
    if answer:
        print(' '.join(map(str, answer)))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
