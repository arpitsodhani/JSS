# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    tokens = list(map(int, sys.stdin.read().split()))
    n = tokens[0]
    records = [
        {
            "speed": tokens[i],
            "ram": tokens[i + 1],
            "hdd": tokens[i + 2],
            "price": tokens[i + 3],
            "id": (i - 1) // 4 + 1,
        }
        for i in range(1, 4 * n + 1, 4)
    ]

    outdated = [False] * n
    for i, first in enumerate(records):
        for second in records:
            if first["speed"] < second["speed"] and first["ram"] < second["ram"] and first["hdd"] < second["hdd"]:
                outdated[i] = True
                break

    chosen = None
    for i, laptop in enumerate(records):
        if not outdated[i] and (chosen is None or laptop["price"] < chosen["price"]):
            chosen = laptop

    sys.stdout.write(str(chosen["id"]))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
