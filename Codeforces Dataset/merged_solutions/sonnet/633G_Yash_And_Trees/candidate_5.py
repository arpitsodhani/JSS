# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def build_prime_mask(m):
            if m <= 2:
                return 0
    
            is_prime = [True] * m
            is_prime[0] = False
            is_prime[1] = False
    
            p = 2
            while p * p < m:
                if is_prime[p]:
                    for x in range(p * p, m, p):
                        is_prime[x] = False
                p += 1
    
            mask = 0
            for i in range(m):
                if is_prime[i]:
                    mask |= 1 << i
            return mask

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            idx = 0
    
            n = data[idx]
            m = data[idx + 1]
            idx += 2
    
            values = [0] + data[idx:idx + n]
            idx += n
    
            graph = [[] for _ in range(n + 1)]
            for _ in range(n - 1):
                u = data[idx]
                v = data[idx + 1]
                idx += 2
                graph[u].append(v)
                graph[v].append(u)
    
            tin = [0] * (n + 1)
            tout = [0] * (n + 1)
            order = []
    
            stack = [(1, 0, 0)]
            while stack:
                v, parent, state = stack.pop()
                if state == 0:
                    tin[v] = len(order)
                    order.append(v)
                    stack.append((v, parent, 1))
                    for to in reversed(graph[v]):
                        if to != parent:
                            stack.append((to, v, 0))
                else:
                    tout[v] = len(order)
    
            all_mask = (1 << m) - 1
            prime_mask = build_prime_mask(m)
    
            size = 1
            while size < n:
                size *= 2
    
            tree = [0] * (2 * size)
            lazy = [0] * (2 * size)
    
            for i, v in enumerate(order):
                tree[size + i] = 1 << (values[v] % m)
    
            for i in range(size - 1, 0, -1):
                tree[i] = tree[2 * i] | tree[2 * i + 1]
    
            def rotate(mask, shift):
                shift %= m
                if shift == 0:
                    return mask
                return ((mask << shift) & all_mask) | (mask >> (m - shift))
    
            def apply(node, shift):
                shift %= m
                if shift:
                    tree[node] = rotate(tree[node], shift)
                    lazy[node] = (lazy[node] + shift) % m
    
            def push(node):
                shift = lazy[node]
                if shift:
                    apply(2 * node, shift)
                    apply(2 * node + 1, shift)
                    lazy[node] = 0
    
            def update(node, left, right, ql, qr, shift):
                if ql <= left and right <= qr:
                    apply(node, shift)
                    return
                push(node)
                mid = (left + right) // 2
                if ql < mid:
                    update(2 * node, left, mid, ql, qr, shift)
                if mid < qr:
                    update(2 * node + 1, mid, right, ql, qr, shift)
                tree[node] = tree[2 * node] | tree[2 * node + 1]
    
            def query(node, left, right, ql, qr):
                if ql <= left and right <= qr:
                    return tree[node]
                push(node)
                mid = (left + right) // 2
                result = 0
                if ql < mid:
                    result |= query(2 * node, left, mid, ql, qr)
                if mid < qr:
                    result |= query(2 * node + 1, mid, right, ql, qr)
                return result
    
            q = data[idx]
            idx += 1
    
            answers = []
            for _ in range(q):
                query_type = data[idx]
                idx += 1
        
                if query_type == 1:
                    v = data[idx]
                    x = data[idx + 1]
                    idx += 2
                    update(1, 0, size, tin[v], tout[v], x % m)
                else:
                    v = data[idx]
                    idx += 1
                    mask = query(1, 0, size, tin[v], tout[v])
                    answers.append(str((mask & prime_mask).bit_count()))
    
            print('\n'.join(answers))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
