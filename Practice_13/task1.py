import string

letter_counts = {char: 0 for char in string.ascii_lowercase}
total_letters = 0

try:
 
    with open('gadsby.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        
        for char in text:
    
            if char.isalpha():
            
                char = char.lower()
                
                if char in letter_counts:
                    letter_counts[char] += 1
                    total_letters += 1

    results = []
    for char, count in letter_counts.items():
        if total_letters > 0:
            percentage = (count / total_letters) * 100
        else:
            percentage = 0
        results.append((char, percentage))

    results.sort(key=lambda x: x[1], reverse=True)


    print("Перші 5 літер : ")
    for char, perc in results[:5]:
       
        print(f"{char}: {perc:.3f}%")

    print("\nОстанні 5 літер : ")
    for char, perc in results[-5:]:
        print(f"{char}: {perc:.3f}%")

except FileNotFoundError:
    print("Помилка: Файл 'gadsby.txt' не знайдено. Перевір, чи він у тій же папці, що і код.")