# CLAUSE: setup_environment
import sys
import heapq

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    t = nums[pos]
    pos += 1
    out = []

    for _ in range(t):
        m = nums[pos]
        x = nums[pos + 1]
        pos += 2

        spent = 0
        taken = []

        for month in range(m):
            cost = nums[pos]
            pos += 1
            available_before_month = month * x

            if spent + cost <= available_before_month:
                spent += cost
                heapq.heappush(taken, -cost)
            elif taken and -taken[0] > cost:
                spent += cost + heapq.heappop(taken)
                heapq.heappush(taken, -cost)

        out.append(str(len(taken)))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
