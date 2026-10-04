import heapq
import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    q = numbers[0]
    cursor = 1
    queries = []
    for _ in range(q):
        kind = numbers[cursor]
        if kind == 1:
            queries.append([1, numbers[cursor + 1]])
            cursor += 2
        else:
            queries.append([kind])
            cursor += 1
    return queries


# --- clause: serve_all :: (queries: list[list[int]]) -> list[int] ---
def serve_all(queries):
    money = [0]
    gone = [False]
    order = []
    front = 0
    out = []
    for query in queries:
        if query[0] == 1:
            money.append(query[1])
            gone.append(False)
            heapq.heappush(order, (-query[1], len(money) - 1))
        elif query[0] == 2:
            front += 1
            while gone[front]:
                front += 1
            gone[front] = True
            out.append(front)
        else:
            while True:
                who = order[0][1]
                if gone[who]:
                    heapq.heappop(order)
                    continue
                heapq.heappop(order)
                gone[who] = True
                out.append(who)
                break
    return out


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(" ".join(map(str, serve_all(read_input()))) + "\n")


if __name__ == "__main__":
    main()
