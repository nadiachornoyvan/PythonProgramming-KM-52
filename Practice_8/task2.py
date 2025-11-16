import math

try:
    a = float(input("Введіть а : "))
    b = float(input("Введіть b : "))
    c = float(input("Введіть c : "))

    D = b**2 - 4*a*c
    print(f"Дискримінант D = {D}")

    if D < 0:
      raise ValueError(f"Дискримінант D = {D:.2f} < 0. Рівняння не має дійсних коренів.") 
    
    elif D == 0:
        x = -b / (2*a)
        print(f"Рівняння має один дійсний корінь: x = {x}")

    else : 
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"Рівняння має два дійсні корені: x1 = {x1}, x2 = {x2}")
        
except ValueError as e:
    print(f"Помилка вхідних даних або обчислення: {e}")
    print("Будь ласка, переконайтеся, що ви вводите числа, і рівняння має дійсні корені.")

except ZeroDivisionError:
    print("Помилка: Ділення на нуль!")
    print("Коефіцієнт 'a' не може дорівнювати нулю для квадратного рівняння.")
    
    if b != 0:
        x_linear = -c / b
        print(f"Це лінійне рівняння (a=0) з одним коренем: x = {x_linear}")

    else:
        if c == 0:
            print("Рівняння має нескінченну кількість розв'язків (0 = 0).")

        else:
            print("Рівняння не має розв'язків (a=0, b=0, c!=0).")

except Exception as e:
    print(f"Виникла неочікувана помилка: {e}")