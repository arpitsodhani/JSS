import sys

def solve():
    html = sys.stdin.read().strip()
    
    # Handle HTML entities if present (though likely not in actual input)
    html = html.replace('&lt;', '<').replace('&gt;', '>')
    
    results = []
    table_stack = []  # Stack of indices in results array
    i = 0
    
    while i < len(html):
        if html[i:i+7] == '<table>':
            results.append(0)
            table_stack.append(len(results) - 1)
            i += 7
        elif html[i:i+8] == '</table>':
            table_stack.pop()
            i += 8
        elif html[i:i+4] == '<td>':
            if table_stack:
                results[table_stack[-1]] += 1
            i += 4
        elif html[i:i+5] == '</td>':
            i += 5
        elif html[i:i+4] == '<tr>':
            i += 4
        elif html[i:i+5] == '</tr>':
            i += 5
        else:
            i += 1
    
    print(' '.join(map(str, results)))

solve()
