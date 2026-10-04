# CLAUSE: setup_environment
import sys
import heapq

MOD = 1000000007

# CLAUSE: solve_logic
def simulate(steps, start):
    seen = set()
    heap = []
    for item in start:
        seen.add(item)
        heap.append(item)
    heapq.heapify(heap)
    value = 1
    done = 0
    while done < steps:
        while heap:
            current = heapq.heappop(heap)
            if current in seen:
                break
        else:
            return value
        seen.remove(current)
        value = value * current % MOD
        added = 1
        while added < current:
            if added not in seen:
                seen.add(added)
                heapq.heappush(heap, added)
            added += 1
        done += 1
    return value

def main():
    stream = iter(map(int, sys.stdin.buffer.read().split()))
    count = next(stream)
    answers = []
    for _ in range(count):
        n = next(stream)
        k = next(stream)
        arr = [next(stream) for _ in range(n)]
        answers.append(str(simulate(k, arr)))
    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
