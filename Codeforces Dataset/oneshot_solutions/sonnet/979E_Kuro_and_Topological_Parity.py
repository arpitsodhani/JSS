import sys

def main():
    data = sys.stdin.buffer.read().decode().split()
    n = int(data[0])
    colors = [int(data[i+1]) for i in range(n)]
    
    unpainted = [i for i in range(n) if colors[i] == -1]
    
    answer = 0
    
    # Try all colorings of unpainted nodes
    for color_mask in range(1 << len(unpainted)):
        col = colors[:]
        for bit, idx in enumerate(unpainted):
            col[idx] = (color_mask >> bit) & 1
        
        # Try all edge configurations
        num_edges = n * (n - 1) // 2
        for edge_mask in range(1 << num_edges):
            # Compute alternating paths mod 2
            f = [1] * n
            
            edge_id = 0
            for i in range(n):
                for j in range(i):
                    has_edge = (edge_mask >> edge_id) & 1
                    edge_id += 1
                    
                    if has_edge and col[j] != col[i]:
                        f[i] ^= f[j]
            
            # Count if total paths is odd
            if sum(f) & 1:
                answer += 1
    
    print(answer)

if __name__ == "__main__":
    main()
