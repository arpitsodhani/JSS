# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def is_outdated(item, all_items):
    speed, ram, hdd = item[0], item[1], item[2]
    for other in all_items:
        if speed < other[0] and ram < other[1] and hdd < other[2]:
            return True
    return False

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    laptops = []
    k = 1
    for number in range(n):
        laptops.append((int(data[k]), int(data[k + 1]), int(data[k + 2]), int(data[k + 3]), number + 1))
        k += 4

    answer = min((laptop for laptop in laptops if not is_outdated(laptop, laptops)), key=lambda x: x[3])
    print(answer[4])

# CLAUSE: finish_program
main()
