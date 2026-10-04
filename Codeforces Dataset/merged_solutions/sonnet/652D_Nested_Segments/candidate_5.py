# CLAUSE: setup_environment
import sys

class CounterTree:
    def __init__(self, size):
        self.data = [0] * (size + 1)
        self.size = size

    def put(self, index):
        while index <= self.size:
            self.data[index] += 1
            index += index & -index

    def take(self, index):
        value = 0
        data = self.data
        while index:
            value += data[index]
            index -= index & -index
        return value

# CLAUSE: solve_logic
def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    n = nums[0]
    records = []
    right_values = []
    for original, start in enumerate(range(1, len(nums), 2)):
        left = nums[start]
        right = nums[start + 1]
        records.append((left, original, right))
        right_values.append(right)

    positions = {}
    for number, right in enumerate(sorted(right_values), 1):
        positions[right] = number

    records = sorted(records, key=lambda item: item[0], reverse=True)
    tree = CounterTree(n)
    answer = [0 for _ in range(n)]

    for left, original, right in records:
        compressed_right = positions[right]
        answer[original] = tree.take(compressed_right - 1)
        tree.put(compressed_right)

    sys.stdout.write("\n".join(str(answer[i]) for i in range(n)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
