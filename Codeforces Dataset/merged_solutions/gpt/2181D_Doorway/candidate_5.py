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

            n = data[0]
            pos = 1
            events = []

            for i in range(n):
                k = data[pos]
                a = data[pos + 1]
                b = data[pos + 2]
                pos += 3

                starts = [a]
                pref = 0
                for _ in range(k):
                    pref += data[pos]
                    pos += 1
                    starts.append(a + pref)

                free = b - a - pref
                for s in starts:
                    events.append((s, i, free))

            events.sort()

            cur = [None] * n
            heap = []
            active = 0
            ans = 0
            m = len(events)
            j = 0

            while j < m:
                x = events[j][0]
                while j < m and events[j][0] == x:
                    _, layer, free = events[j]
                    value = x + free
                    if cur[layer] is None:
                        active += 1
                    cur[layer] = value
                    heapq.heappush(heap, (value, layer))
                    j += 1

                while heap and cur[heap[0][1]] != heap[0][0]:
                    heapq.heappop(heap)

                if active == n:
                    val = heap[0][0] - x
                    if val > ans:
                        ans = val

            print(ans)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
