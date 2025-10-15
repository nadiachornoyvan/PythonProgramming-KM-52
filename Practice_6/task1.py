first_phrase = input('перша фраза : ')
second_phrase = input('друга фраза : ')

new_first_phrase = first_phrase.lower().replace(' ', '')
new_second_phrase = second_phrase.lower().replace(' ', '')

if new_first_phrase.isalpha():
    print()
else:
    print('Помилка у першомій фразі, перевірте, будь ласка, відсутніть інших символів окрім літер')
    exit()

if new_second_phrase.isalpha():
    print()
else:
    print('Помилка у другій фразі, перевірте, будь ласка, відсутніть інших символів окрім літер')
    exit()


first_leters = set(new_first_phrase)
second_leters = set(new_second_phrase)



print('літери першої фрази:', first_leters, ', кількість унікальних літер у першій фразі :', len(first_leters))
print('літери другої фрази:', second_leters, ', кількість унікальних літер у другій фразі:', len(second_leters))

issubset = second_leters.issubset(first_leters)
if issubset is True :
   print('З літер першого слова можна скласти другу фразу')
else :
    print('З літер першого слова неможливо скласти другу фразу')
    exit

