# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
def read_numbers():
    for item in sys.stdin.buffer.read().split():
        yield int(item)

def main():
    nums = read_numbers()
    n = next(nums)
    m = next(nums)

    begin = defaultdict(list)
    finish = defaultdict(list)

    for _ in range(n):
        a = next(nums)
        h = next(nums)
        left = next(nums)
        right = next(nums)

        if left < 100:
            keep = (100 - left) / 100.0
            begin[a - h].append(keep)
            finish[a].append(keep)

        if right < 100:
            keep = (100 - right) / 100.0
            begin[a + 1].append(keep)
            finish[a + h + 1].append(keep)

    mushrooms = []
    for _ in range(m):
        mushrooms.append((next(nums), next(nums)))

    mushrooms.sort()
    keys = sorted(set(begin) | set(finish) | {x for x, _ in mushrooms})

    by_place = defaultdict(int)
    for x, z in mushrooms:
        by_place[x] += z

    alive = 1.0
    answer = 0.0

    for x in keys:
        for keep in begin[x]:
            alive *= keep
        for keep in finish[x]:
            alive /= keep
        if x in by_place:
            answer += by_place[x] * alive

    sys.stdout.write(f"{answer:.10f}")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
