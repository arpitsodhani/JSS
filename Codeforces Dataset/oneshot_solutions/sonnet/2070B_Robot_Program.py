import sys

def simulate_from_position(start_pos, commands, max_seconds):
    position = start_pos
    zeros = 0
    cmd_idx = 0
    seconds = 0
    n = len(commands)
    
    while seconds < max_seconds:
        if commands[cmd_idx] == 'L':
            position -= 1
        else:
            position += 1
        seconds += 1
        
        if position == 0:
            zeros += 1
            return (zeros, 0, seconds, False)
        
        cmd_idx += 1
        if cmd_idx >= n:
            return (zeros, position, seconds, True)
    
    return (zeros, position, seconds, False)

def solve():
    input_data = sys.stdin.buffer.read().decode().strip().split('\n')
    t = int(input_data[0])
    
    results = []
    for i in range(1, t + 1):
        line = input_data[i]
        parts = line.split()
        n = int(parts[0])
        x = int(parts[1])
        k_and_commands = parts[2]
        
        for j, ch in enumerate(k_and_commands):
            if not ch.isdigit():
                k = int(k_and_commands[:j])
                commands = k_and_commands[j:]
                break
        
        total_zeros = 0
        remaining_seconds = k
        
        zeros, pos, secs, completed = simulate_from_position(x, commands, remaining_seconds)
        total_zeros += zeros
        remaining_seconds -= secs
        
        if completed or remaining_seconds == 0:
            results.append(str(total_zeros))
            continue
        
        zeros, pos, secs, completed = simulate_from_position(0, commands, remaining_seconds)
        
        if completed or secs == 0:
            total_zeros += zeros
            results.append(str(total_zeros))
            continue
        
        cycle_zeros = zeros
        cycle_length = secs
        
        full_cycles = remaining_seconds // cycle_length
        total_zeros += full_cycles * cycle_zeros
        remaining_seconds = remaining_seconds % cycle_length
        
        if remaining_seconds > 0:
            zeros, pos, secs, completed = simulate_from_position(0, commands, remaining_seconds)
            total_zeros += zeros
        
        results.append(str(total_zeros))
    
    print('\n'.join(results))

solve()
