# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    laptops = []
    pos = 1
    for index in range(1, n + 1):
        speed, ram, hdd, price = values[pos:pos + 4]
        pos += 4
        laptops.append((speed, ram, hdd, price, index))

    best_price = 10 ** 30
    best_index = -1

    for speed, ram, hdd, price, index in laptops:
        outdated = False
        for other_speed, other_ram, other_hdd, _, _ in laptops:
            if speed < other_speed and ram < other_ram and hdd < other_hdd:
                outdated = True
                break
        if not outdated and price < best_price:
            best_price = price
            best_index = index

    sys.stdout.write(str(best_index))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
