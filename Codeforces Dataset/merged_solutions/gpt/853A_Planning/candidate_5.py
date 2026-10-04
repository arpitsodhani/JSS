# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        import heapq

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            if not data:
                return

            n, k = data[0], data[1]
            c = data[2:2 + n]

            heap = []
            ans = [0] * n
            total = 0

            initial = min(n, k + 1)
            for i in range(initial):
                heapq.heappush(heap, (-c[i], i))

            nxt = k + 1

            for t in range(k + 1, k + n + 1):
                if nxt < n:
                    heapq.heappush(heap, (-c[nxt], nxt))
                    nxt += 1

                cost, idx = heapq.heappop(heap)
                ans[idx] = t
                total += (-cost) * (t - (idx + 1))

            print(total)
            print(*ans)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
