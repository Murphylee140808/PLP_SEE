#year = int(input("Enter a year to check if a year is leap or not: "))

#if year % 4 == 0:
    #print("It's a leap year!")

#else:
    #print("It's not a leap year")


def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True  # Divisible by 400 → Leap year
            else:
                return False  # Divisible by 100 but not 400 → Not a leap year
        else:
            return True  # Divisible by 4 but not 100 → Leap year
    else:
        return False  # Not divisible by 4 → Not a leap year

# Example usage
year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")