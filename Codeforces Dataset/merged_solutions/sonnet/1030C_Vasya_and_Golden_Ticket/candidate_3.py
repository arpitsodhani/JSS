# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
items = sys.stdin.read().split()
answer = "NO"
if items:
    s = items[-1] if len(items) > 1 else items[0]
    n = len(s)
    prefix = [0]
    for ch in s:
        prefix.append(prefix[-1] + int(ch))
    total = prefix[-1]
    for cut in range(1, n):
        target = prefix[cut]
        if target == 0:
            answer = "YES"
            break
        if total % target != 0:
            continue
        needed = target
        ok = True
        count = 1
        for value in prefix[cut + 1:]:
            if value == needed + target:
                needed += target
                count += 1
            elif value > needed + target:
                ok = False
                break
        if ok and needed == total and count >= 2:
            answer = "YES"
            break

# CLAUSE: finish_program
if items:
    sys.stdout.write(answer)
