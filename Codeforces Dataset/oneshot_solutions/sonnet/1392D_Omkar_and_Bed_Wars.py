import sys

def count_changes(s):
    n = len(s)
    if n == 0:
        return 0
    
    # Find all runs
    runs = []
    i = 0
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        runs.append(j - i)
        i = j
    
    # Special case: only one run (all same character)
    if len(runs) == 1:
        return (n + 2) // 3
    
    # Check if first and last runs merge (circular)
    changes = 0
    if s[0] == s[n - 1]:
        # Merge first and last runs
        total_length = runs[0] + runs[-1]
        if total_length >= 3:
            changes += (total_length + 2) // 3
        # Add changes for middle runs (non-circular)
        for i in range(1, len(runs) - 1):
            if runs[i] >= 3:
                changes += (runs[i] + 1) // 3
    else:
        # No circular run, all runs are non-circular
        for length in runs:
            if length >= 3:
                changes += (length + 1) // 3
    
    return changes

def main():
    input_data = sys.stdin.read().strip().split('\n')
    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        n = int(input_data[idx])
        s = input_data[idx + 1]
        idx += 2
        print(count_changes(s))

if __name__ == "__main__":
    main()
