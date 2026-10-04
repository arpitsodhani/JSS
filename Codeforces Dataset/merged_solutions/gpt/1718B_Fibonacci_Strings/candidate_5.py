# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        import heapq

        def solve():
            data = list(map(int, sys.stdin.buffer.read().split()))
            t = data[0]
            pos = 1

            fib = [1, 1]
            while fib[-1] <= 10**11 + 1:
                fib.append(fib[-1] + fib[-2])

            index = {v: i for i, v in enumerate(fib)}

            ans = []
            for _ in range(t):
                k = data[pos]
                pos += 1
                c = data[pos:pos + k]
                pos += k

                s = sum(c)
                if s + 1 not in index:
                    ans.append("NO")
                    continue

                idx = index[s + 1]
                needs = fib[:idx - 1][::-1]

                heap = [(-x, i) for i, x in enumerate(c)]
                heapq.heapify(heap)

                blocked = None
                ok = True

                for need in needs:
                    if not heap:
                        ok = False
                        break

                    neg, i = heapq.heappop(heap)
                    cur = -neg

                    if cur < need:
                        ok = False
                        break

                    cur -= need

                    if blocked is not None:
                        heapq.heappush(heap, blocked)

                    blocked = (-cur, i) if cur > 0 else None

                ans.append("YES" if ok else "NO")

            sys.stdout.write("\n".join(ans))

        if __name__ == "__main__":
            solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
