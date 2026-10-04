# CLAUSE: setup_environment
import sys

def receive():
    return int(sys.stdin.readline())

def send(text):
    print(text, flush=True)

# CLAUSE: solve_logic
def solve():
    first = receive()
    positions = [(first, 0)]
    known = {first}
    now = first

    for distance in range(1, 11):
        send("+ 1")
        now = receive()
        if now == first:
            send("! " + str(distance))
            return
        if now not in known:
            known.add(now)
            positions.append((now, distance))

    found = dict(positions)
    for blocks in range(1, 991):
        send("- 1010")
        now = receive()
        if now in found:
            total = found[now] + blocks * 1010 - 10
            if total > 0:
                send("! " + str(total))
                return

# CLAUSE: finish_program
solve()
