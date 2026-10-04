# CLAUSE: setup_environment
import sys
import heapq

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    n = nums[0]
    starts = [0] * n
    sizes = [0] * n
    priorities = [0] * n
    taken = set()
    hidden = -1
    at = 1

    for i in range(n):
        starts[i] = nums[at]
        sizes[i] = nums[at + 1]
        priorities[i] = nums[at + 2]
        at += 3
        if priorities[i] == -1:
            hidden = i
        else:
            taken.add(priorities[i])

    deadline = nums[at]
    hidden_start = starts[hidden]
    hidden_size = sizes[hidden]
    sorted_jobs = sorted((starts[i], sizes[i], priorities[i]) for i in range(n) if i != hidden)

    def calculated_finish(candidate):
        now = hidden_start
        rest = hidden_size
        ahead = 0
        active_before = 0
        last_time = 0

        for arrive, amount, pri in sorted_jobs:
            if pri <= candidate:
                continue

            if arrive < hidden_start:
                if active_before:
                    ahead = max(0, ahead - (arrive - last_time))
                active_before = 1
                ahead += amount
                last_time = arrive
                continue

            if active_before:
                ahead = max(0, ahead - (hidden_start - last_time))
                active_before = 0

            while now < arrive:
                if ahead:
                    use = min(ahead, arrive - now)
                    ahead -= use
                    now += use
                else:
                    use = arrive - now
                    if rest <= use:
                        return now + rest
                    rest -= use
                    now = arrive

            ahead += amount

        if active_before:
            ahead = max(0, ahead - (hidden_start - last_time))

        return now + ahead + rest

    low = -10 ** 18
    high = 10 ** 18
    while low < high:
        middle = low + (high - low) // 2
        if calculated_finish(middle) <= deadline:
            high = middle
        else:
            low = middle + 1

    final_priority = low
    while final_priority in taken:
        final_priority += 1

    priorities[hidden] = final_priority

    ids = list(range(n))
    ids.sort(key=lambda x: starts[x])
    left = sizes[:]
    end = [0] * n
    heap = []
    time = 0
    pointer = 0

    while pointer < n or heap:
        if not heap and pointer < n:
            if time < starts[ids[pointer]]:
                time = starts[ids[pointer]]

        while pointer < n and starts[ids[pointer]] <= time:
            item = ids[pointer]
            heapq.heappush(heap, (-priorities[item], item))
            pointer += 1

        neg, item = heapq.heappop(heap)
        next_time = starts[ids[pointer]] if pointer < n else 10 ** 30
        span = next_time - time

        if span < left[item]:
            left[item] -= span
            time = next_time
            heapq.heappush(heap, (neg, item))
        else:
            time += left[item]
            left[item] = 0
            end[item] = time

    sys.stdout.write(str(final_priority))
    sys.stdout.write("\n")
    sys.stdout.write(" ".join(map(str, end)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
