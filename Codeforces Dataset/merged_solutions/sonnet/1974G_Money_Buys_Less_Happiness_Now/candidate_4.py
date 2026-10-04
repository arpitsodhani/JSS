# CLAUSE: setup_environment
import sys
import heapq

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    cases = int(next(it))
    answer_lines = []

    for _ in range(cases):
        m = int(next(it))
        x = int(next(it))
        current_month = 0
        total_cost = 0
        buys = []

        while current_month < m:
            c = int(next(it))
            if total_cost + c <= current_month * x:
                total_cost += c
                heapq.heappush(buys, -c)
            elif buys and -buys[0] > c:
                total_cost += c + heapq.heapreplace(buys, -c)
            current_month += 1

        answer_lines.append(str(len(buys)))

    sys.stdout.write("\n".join(answer_lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
