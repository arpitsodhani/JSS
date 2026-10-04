# CLAUSE: setup_environment
import sys

def answer_queries(a, queries):
    n = len(a)
    rank = sorted(range(n), key=lambda i: (-a[i], i))
    chosen_rank = [0] * n
    for t, idx in enumerate(rank, 1):
        chosen_rank[idx] = t
    responses = []
    cache = {}

# CLAUSE: solve_logic
    for k, pos in queries:
        if k not in cache:
            seq = []
            for i, value in enumerate(a):
                if chosen_rank[i] <= k:
                    seq.append(value)
            cache[k] = seq
        responses.append(str(cache[k][pos - 1]))
    return responses

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    m_index = 1 + n
    m = int(data[m_index])
    raw = data[m_index + 1:]
    queries = [(int(raw[i]), int(raw[i + 1])) for i in range(0, 2 * m, 2)]

# CLAUSE: finish_program
    sys.stdout.write("\n".join(answer_queries(a, queries)))

if __name__ == "__main__":
    main()
