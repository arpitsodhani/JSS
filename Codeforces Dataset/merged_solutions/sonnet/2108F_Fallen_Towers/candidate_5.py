# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def possible(arr, size, target):
    end_events = [0] * (size + 1)
    added = 0
    first_positive = size - target + 1
    for index in range(size):
        added -= end_events[index]
        wanted = index - first_positive + 1
        if wanted < 0:
            wanted = 0
        if added < wanted:
            return False
        reach = index + arr[index] + added - wanted + 1
        added += 1
        if reach < size:
            end_events[reach] += 1
    return True

def best_mex(size, arr):
    ok = 1
    bad = size + 1
    while bad - ok > 1:
        probe = (ok + bad) // 2
        if possible(arr, size, probe):
            ok = probe
        else:
            bad = probe
    return ok

def main():
    raw = sys.stdin.buffer.read().split()
    pos = 0
    count = int(raw[pos])
    pos += 1
    ans = [""] * count
    for case in range(count):
        n = int(raw[pos])
        pos += 1
        arr = []
        for _ in range(n):
            arr.append(int(raw[pos]))
            pos += 1
        ans[case] = str(best_mex(n, arr))
    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
