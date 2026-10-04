# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    socks = data[1:]

    on_table = set()
    ans = 0

    for x in socks:
        if x in on_table:
            on_table.remove(x)
        else:
            on_table.add(x)
            ans = max(ans, len(on_table))

    print(ans)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
