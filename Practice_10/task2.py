import numpy as np

def leap_year(year):
    """Функція, що визначає, чи є рік високосним"""
    return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))

def get_leap_years(years_list):
    """Функція, що повертає список високосних років"""
    leap_years_np = list(filter(leap_year, years_list))
    leap_years_int = list(map(int, leap_years_np))
    return leap_years_int

def get_days_in_month(leap_year_func, month, year):
    """Функція, що визначає кількість днів у місяці"""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if leap_year_func(year):
            return 29
        else:
            return 28

def main():
    """Головна функція виконання скрипту"""
    years = np.arange(1900, 2020 + 5, 1)
    
    print("Список високосних років (1900-2024):")
    print(get_leap_years(years))
    print("-" * 30) 

    try:
        month = int(input("Enter the month number (1-12): "))
        year = int(input("Enter the year (4 digits):"))
        
        if not 1 <= month <= 12:
            print("Error. The month number must be between 1 and 12")
        elif not 1000 <= year <= 9999:
            print("Error. The year must be a four-digit number")
        else:
            days = get_days_in_month(leap_year, month, year)
            print(f"Number of days in {month} months of {year} : {days}")
            
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()