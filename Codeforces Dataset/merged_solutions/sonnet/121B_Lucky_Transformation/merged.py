import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    digits = list(data[2].decode())
    return n, k, digits

# Clause transform [Confidence: 1.00]
def transform(n, k, digits):
    i = 0
    while i + 1 < n and k > 0:
        if digits[i] == "4" and digits[i + 1] == "7":
            if i % 2 == 0:
                if i + 2 < n and digits[i + 2] == "7":
                    if k % 2 == 1:
                        digits[i + 1] = "4"
                    break
                digits[i + 1] = "4"
            else:
                if digits[i - 1] == "4":
                    if k % 2 == 1:
                        digits[i] = "7"
                        digits[i + 1] = "7"
                    break
                digits[i] = "7"
                digits[i + 1] = "7"
            k -= 1
        i += 1
    return "".join(digits)

# Clause main [Confidence: 1.00]
def main():
    n, k, digits = read_input()
    sys.stdout.write(transform(n, k, digits) + "\n")


if __name__ == "__main__":
    main()

