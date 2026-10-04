import sys
from itertools import permutations

def is_valid_date(day, month, year):
    if month < 1 or month > 12:
        return False
    if day < 1:
        return False
    
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check for leap year
    if month == 2:
        if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    else:
        if day > days_in_month[month - 1]:
            return False
    
    return True

def convert_year(yy):
    if yy >= 50:
        return 1900 + yy
    else:
        return 2000 + yy

def is_at_least_18(birth_day, birth_month, birth_year, finals_day, finals_month, finals_year):
    age = finals_year - birth_year
    if age > 18:
        return True
    elif age == 18:
        if finals_month > birth_month:
            return True
        elif finals_month == birth_month:
            return finals_day >= birth_day
        else:
            return False
    else:
        return False

# Read input
lines = sys.stdin.read().strip().split('\n')
finals_parts = lines[0].split('.')
birth_parts = lines[1].split('.')

finals_day = int(finals_parts[0])
finals_month = int(finals_parts[1])
finals_yy = int(finals_parts[2])

birth_components = [int(birth_parts[0]), int(birth_parts[1]), int(birth_parts[2])]

finals_year = convert_year(finals_yy)

# Try all permutations
found = False
for perm in permutations(birth_components):
    day, month, year_yy = perm
    year = convert_year(year_yy)
    
    if is_valid_date(day, month, year) and year <= finals_year:
        if is_at_least_18(day, month, year, finals_day, finals_month, finals_year):
            found = True
            break

if found:
    print("YES")
else:
    print("NO")
