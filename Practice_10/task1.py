salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
percent = 0.30

def new_salary_list(old_salary):
    """
    Розраховує нову зарплату, збільшену на 30%, 
    округлену до найближчої сотої.
    """
    
    new_salary = old_salary * (percent + 1)
    return round(new_salary, 2)

def increase_amount(old_salary):
    """
    Розраховує суму індексації (30% від старої зарплати), 
    округлену до найближчої сотої.
    """
    
    increase = old_salary * percent
    return round(increase, 2)


if __name__ == "__main__":
    
    
    new_salaries = [new_salary_list(salary) for salary in salary_list]
    increase_amounts = [increase_amount(salary) for salary in salary_list]

    print("Salary table:")
    
  
    for old, new, increase in zip(salary_list, new_salaries, increase_amounts):
        print(old, new, increase)