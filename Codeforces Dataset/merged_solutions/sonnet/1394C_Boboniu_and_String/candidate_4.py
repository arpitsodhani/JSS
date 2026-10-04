# CLAUSE: setup_environment
import sys

def main():
    items = sys.stdin.read().strip().split()
    arr = items[1:]
    values = [(len(s), s.count('B') * 2 - len(s)) for s in arr]

# CLAUSE: solve_logic
    def intersection(rad):
        lower_len = max([1] + [x - rad for x, y in values])
        upper_len = min(x + rad for x, y in values)
        lower_bal = max(y - rad for x, y in values)
        upper_bal = min(y + rad for x, y in values)
        if lower_len > upper_len or lower_bal > upper_bal:
            return None
        first_len = lower_len
        second_len = min(upper_len, lower_len + 1)
        for length in range(first_len, second_len + 1):
            balance = lower_bal
            if balance % 2 != length % 2:
                balance += 1
            if balance <= upper_bal:
                count_b = (length + balance) // 2
                count_n = length - count_b
                if count_b >= 0 and count_n >= 0 and length > 0:
                    return count_b, count_n
        return None

    low = 0
    high = max((len(s) for s in arr), default=0) + 1000000
    while low < high:
        middle = low + (high - low) // 2
        got = intersection(middle)
        if got is None:
            low = middle + 1
        else:
            high = middle
    result = intersection(low)

# CLAUSE: finish_program
    sys.stdout.write("{}\n{}\n".format(low, "B" * result[0] + "N" * result[1]))

if __name__ == "__main__":
    main()
