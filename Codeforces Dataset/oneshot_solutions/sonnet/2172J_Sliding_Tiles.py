import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    
    n = int(input_data[idx])
    idx += 1
    
    a = list(map(int, input_data[idx:idx+n]))
    idx += n
    
    h = list(map(int, input_data[idx:idx+n-1]))
    
    # After tilt right and tilt down, column_counts[col] = number of tiles in column col
    column_counts = [0] * n
    
    # Process each row
    for row in range(n):
        # Find segments for this row (bars with height > row block movement)
        segments = []
        start = 0
        for i in range(n - 1):
            if h[i] > row:  # bar blocks this row
                segments.append((start, i))
                start = i + 1
        segments.append((start, n - 1))
        
        # For each segment, count tiles and pack them to the right
        for seg_start, seg_end in segments:
            # Count tiles in this segment for this row
            tiles_in_segment = 0
            for col in range(seg_start, seg_end + 1):
                if row < a[col]:  # column col has a tile at this row
                    tiles_in_segment += 1
            
            # Pack tiles to the right of segment
            pos = seg_end
            for _ in range(tiles_in_segment):
                column_counts[pos] += 1
                pos -= 1
    
    print(' '.join(map(str, column_counts)))

solve()
