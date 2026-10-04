# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def solve():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        t = data[0]
        idx = 1
        out = []

        for _ in range(t):
            n = data[idx]
            idx += 1
            a = data[idx:idx + n]
            idx += n

            rem = {}
            for x in a:
                rem[x] = rem.get(x, 0) + 1

            required = set()
            segments = 0
            pos = 0

            while pos < n:
                current = set()
                seen_required = set()
                missing = len(required)
                dead = 0
                dead_set = set()
                cut = -1

                while pos < n:
                    x = a[pos]
                    rem[x] -= 1

                    if x not in current:
                        current.add(x)
                        if rem[x] == 0:
                            dead += 1
                            dead_set.add(x)
                    elif rem[x] == 0 and x not in dead_set:
                        dead += 1
                        dead_set.add(x)

                    if x in required and x not in seen_required:
                        seen_required.add(x)
                        missing -= 1

                    pos += 1

                    if missing == 0 and dead == 0:
                        cut = pos
                        break

                if cut == -1:
                    segments += 1
                    break

                segments += 1
                required = current

            out.append(str(segments))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
