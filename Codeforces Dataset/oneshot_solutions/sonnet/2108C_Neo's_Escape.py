import sys

def solve(n, a):
    # Create list of (weight, position)
    buttons = [(a[i], i+1) for i in range(n)]
    # Sort by weight (decreasing), then by position (increasing)
    buttons.sort(key=lambda x: (-x[0], x[1]))
    
    clones = set()
    pressed = set()
    clones_created = 0
    
    for weight, pos in buttons:
        # Try to find a clone that can reach pos
        can_reach = False
        for clone_pos in list(clones):
            # Check if all positions between clone_pos and pos are pressed
            if clone_pos < pos:
                can_move = all(p in pressed for p in range(clone_pos + 1, pos))
            else:
                can_move = all(p in pressed for p in range(pos + 1, clone_pos))
            
            if can_move:
                # Move this clone to pos
                clones.remove(clone_pos)
                clones.add(pos)
                can_reach = True
                break
        
        if not can_reach:
            # Create a new clone at pos
            clones.add(pos)
            clones_created += 1
        
        pressed.add(pos)
    
    return clones_created

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        results.append(solve(n, a))
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    main()
