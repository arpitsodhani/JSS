import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    
    n = int(input_data[idx])
    m = int(input_data[idx + 1])
    idx += 2
    
    # Build ip to name mapping
    ip_to_name = {}
    for _ in range(n):
        name = input_data[idx]
        ip = input_data[idx + 1]
        ip_to_name[ip] = name
        idx += 2
    
    # Process commands
    results = []
    for _ in range(m):
        command = input_data[idx]
        ip_with_semicolon = input_data[idx + 1]
        idx += 2
        
        # Remove the semicolon to get the ip
        ip = ip_with_semicolon[:-1]
        
        # Get the server name
        name = ip_to_name[ip]
        
        # Format output
        output_line = f"{command} {ip_with_semicolon} #{name}"
        results.append(output_line)
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
