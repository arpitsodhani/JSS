# CLAUSE: setup_environment
import sys

def find_key(left, right, encrypted):
    width = right - left + 1
    maximum = max(encrypted)
    if right > maximum:
        maximum = right
    if left > maximum:
        maximum = left
    limit = 1
    while limit <= maximum:
        limit *= 2
    seen = [0] * width
    token = 0
    for key in range(limit):
        token += 1
        valid = True
        for encrypted_value in encrypted:
            restored = encrypted_value ^ key
            slot = restored - left
            if slot < 0 or slot >= width or seen[slot] == token:
                valid = False
                break
            seen[slot] = token
        if valid:
            return key
    return 0

# CLAUSE: solve_logic
def main():
    stream = iter(map(int, sys.stdin.buffer.read().split()))
    tests = next(stream)
    results = []
    for _ in range(tests):
        left = next(stream)
        right = next(stream)
        amount = right - left + 1
        encrypted = [next(stream) for _ in range(amount)]
        results.append(str(find_key(left, right, encrypted)))
    sys.stdout.write("\n".join(results))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
