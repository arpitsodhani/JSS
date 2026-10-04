import sys

def max_power_of_2_exponent(num):
    """Returns the exponent k such that 2^k is the max power of 2 dividing num"""
    if num % 2 != 0:
        return 0
    
    k = 0
    while num % 2 == 0:
        k += 1
        num //= 2
    return k

def main():
    input_data = sys.stdin.read().strip().split()
    n = int(input_data[0])
    numbers = [int(input_data[i]) for i in range(1, n + 1)]
    
    # Find the exponent of max power of 2 for each number
    exponents = [max_power_of_2_exponent(num) for num in numbers]
    
    # Find the maximum exponent
    max_exp = max(exponents)
    
    # Count how many numbers have this max exponent
    count = exponents.count(max_exp)
    
    # The max power is 2^max_exp
    max_power = 2 ** max_exp
    
    print(max_power, count)

if __name__ == "__main__":
    main()
