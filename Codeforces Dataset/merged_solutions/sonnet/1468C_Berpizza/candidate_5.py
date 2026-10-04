import heapq
import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    q = raw[0]
    reader = 1
    queries = []
    for _ in range(q):
        kind = raw[reader]
        if kind == 1:
            queries.append([1, raw[reader + 1]])
            reader += 2
        else:
            queries.append([kind])
            reader += 1
    return queries


# --- clause: serve_all :: (queries: list[list[int]]) -> list[int] ---
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


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(" ".join(map(str, serve_all(read_input()))) + "\n")


if __name__ == "__main__":
    main()
