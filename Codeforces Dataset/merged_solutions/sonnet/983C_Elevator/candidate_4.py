# CLAUSE: setup_environment
import sys
from heapq import heappop, heappush

def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    if not raw:
        return
    n = raw[0]
    starts = []
    ends = []
    for i in range(n):
        starts.append(raw[1 + 2 * i])
        ends.append(raw[2 + 2 * i])

# CLAUSE: solve_logic
    pow5 = [1] * 10
    for i in range(2, 10):
        pow5[i] = pow5[i - 1] * 5
    limit = pow5[9] * 5

    count_cache = [None] * limit
    size_cache = [-1] * limit
    dest_cache = [None] * limit

    def decode(code):
        cached = count_cache[code]
        if cached is not None:
            return cached
        arr = [0] * 10
        total = 0
        active = []
        for f in range(1, 10):
            v = (code // pow5[f]) % 5
            arr[f] = v
            total += v
            if v:
                active.append(f)
        count_cache[code] = arr
        size_cache[code] = total
        dest_cache[code] = active
        return arr

    def size_of(code):
        if size_cache[code] < 0:
            decode(code)
        return size_cache[code]

    def destinations_of(code):
        if dest_cache[code] is None:
            decode(code)
        return dest_cache[code]

    def add_waiting(pos, target, code, load):
        entered = 0
        while pos < n and load < 4 and starts[pos] == target:
            code += pow5[ends[pos]]
            load += 1
            entered += 1
            pos += 1
        return pos, code, entered

    def key_of(pos, floor, code):
        return ((pos * 9 + floor - 1) * limit + code)

    start_key = key_of(0, 1, 0)
    heap = [(0, 0, 1, 0)]
    best = {start_key: 0}
    answer = 0

    while heap:
        elapsed, pos, floor, code = heappop(heap)
        if best.get(key_of(pos, floor, code)) != elapsed:
            continue
        if pos == n and code == 0:
            answer = elapsed
            break

        counts = decode(code)
        for target in destinations_of(code):
            leaving = counts[target]
            reduced = code - leaving * pow5[target]
            load = size_of(reduced)
            npos, ncode, entered = add_waiting(pos, target, reduced, load)
            ncost = elapsed + abs(floor - target) + leaving + entered
            nkey = key_of(npos, target, ncode)
            if ncost < best.get(nkey, 10 ** 30):
                best[nkey] = ncost
                heappush(heap, (ncost, npos, target, ncode))

        if pos < n:
            target = starts[pos]
            if counts[target] == 0 and size_of(code) < 4:
                npos, ncode, entered = add_waiting(pos, target, code, size_of(code))
                ncost = elapsed + abs(floor - target) + entered
                nkey = key_of(npos, target, ncode)
                if ncost < best.get(nkey, 10 ** 30):
                    best[nkey] = ncost
                    heappush(heap, (ncost, npos, target, ncode))

# CLAUSE: finish_program
    print(answer)

if __name__ == "__main__":
    main()
