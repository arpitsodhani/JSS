import sys

def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def main():
    y = int(sys.stdin.readline())
    
    target_leap = is_leap(y)
    shift = 0
    year = y
    
    while True:
        shift = (shift + (366 if is_leap(year) else 365)) % 7
        year += 1
        
        if shift == 0 and is_leap(year) == target_leap:
            print(year)
            return

if __name__ == "__main__":
    main()
