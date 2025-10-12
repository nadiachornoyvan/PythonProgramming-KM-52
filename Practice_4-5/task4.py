salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
percent = 0.3
indexation_amount_list = []
new_salary_list = []

for i in salary_list :
    indexation_amount = i * percent
    round_indexation_amount = round(indexation_amount, 2)
    indexation_amount_list.append(round_indexation_amount)
    salary = i + round_indexation_amount
    round_salary = round(salary, 2)
    new_salary_list.append(round_salary)

print('Salary table:')

for salary_list, new_salary_list, indexation_amount_list in zip (salary_list, new_salary_list, indexation_amount_list):
    print()
    print(f"{salary_list} {new_salary_list} {indexation_amount_list}")




