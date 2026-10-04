import sys

def find_max_independent_subset(S):
    MAX_LOG = 30
    reduced_basis = [0] * MAX_LOG
    selected = []
    
    for s in S:
        cur = s
        # Reduce cur modulo current basis
        for i in range(MAX_LOG - 1, -1, -1):
            if (cur & (1 << i)) and (reduced_basis[i] != 0):
                cur ^= reduced_basis[i]
        
        # If cur != 0, s is linearly independent
        if cur != 0:
            # Store reduced form for future reductions
            for i in range(MAX_LOG - 1, -1, -1):
                if cur & (1 << i):
                    reduced_basis[i] = cur
                    break
            # Add original s to selected set
            selected.append(s)
    
    return selected

def construct_gray_code_path(basis):
    k = len(basis)
    if k == 0:
        return [0]
    
    path = [0]
    current = 0
    
    for i in range(1, 1 << k):
        # Determine which bit flipped in binary counter
        changed_bits = i ^ (i - 1)
        bit_position = changed_bits.bit_length() - 1
        # XOR with corresponding basis element
        current ^= basis[bit_position]
        path.append(current)
    
    return path

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    S = [int(data[i]) for i in range(1, n + 1)]
    
    basis = find_max_independent_subset(S)
    path = construct_gray_code_path(basis)
    
    print(len(basis))
    print(' '.join(map(str, path)))

if __name__ == '__main__':
    main()
