import heapq
import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    q = data[0]
    pos = 1
    queries = []
    for _ in range(q):
        kind = data[pos]
        if kind == 1:
            queries.append([1, data[pos + 1]])
            pos += 2
        else:
            queries.append([kind])
            pos += 1
    return queries

# Clause serve_all [Confidence: 1.00]
def serve_all(queries):
    served = []
    heap = []
    done = [False]
    plain = 0
    lines = []
    for query in queries:
        if query[0] == 1:
            done.append(False)
            heapq.heappush(heap, (-query[1], len(done) - 1))
        elif query[0] == 2:
            plain += 1
            while done[plain]:
                plain += 1
            done[plain] = True
            lines.append(plain)
        else:
            while heap and done[heap[0][1]]:
                heapq.heappop(heap)
            money, who = heapq.heappop(heap)
            done[who] = True
            lines.append(who)
    return lines

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(" ".join(map(str, serve_all(read_input()))) + "\n")


if __name__ == "__main__":
    main()

