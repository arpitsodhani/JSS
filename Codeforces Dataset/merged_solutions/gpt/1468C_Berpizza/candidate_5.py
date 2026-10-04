# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        import heapq

        def main():
            input = sys.stdin.readline
            q = int(input())
            served = [False] * (q + 2)
            heap = []
            first_unserved = 1
            customer_id = 0
            ans = []

            for _ in range(q):
                query = input().split()
                t = int(query[0])

                if t == 1:
                    customer_id += 1
                    money = int(query[1])
                    heapq.heappush(heap, (-money, customer_id))
                elif t == 2:
                    while served[first_unserved]:
                        first_unserved += 1
                    served[first_unserved] = True
                    ans.append(str(first_unserved))
                else:
                    while served[heap[0][1]]:
                        heapq.heappop(heap)
                    _, idx = heapq.heappop(heap)
                    served[idx] = True
                    ans.append(str(idx))

            print(" ".join(ans))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
