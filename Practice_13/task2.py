import zipfile

top_males_count = {}
top_females_count = {}

try:

    with zipfile.ZipFile('archive.zip', 'r') as archive:

        file_list = archive.namelist()
        
        for filename in file_list:

            if filename.endswith('.txt'):
                
                max_m_count = -1
                best_m_name = ""
                
                max_f_count = -1
                best_f_name = ""
       
                with archive.open(filename) as file:
                    for line in file:
                     
                        text_line = line.decode('utf-8').strip()
                        
                        parts = text_line.split(',')
                        
                        if len(parts) == 3:
                            name = parts[0]
                            sex = parts[1]
                            count = int(parts[2])
                            
                            if sex == 'M':
                                if count > max_m_count:
                                    max_m_count = count
                                    best_m_name = name
                                    
                            elif sex == 'F':
                                if count > max_f_count:
                                    max_f_count = count
                                    best_f_name = name
                
                if best_m_name:
                    if best_m_name in top_males_count:
                        top_males_count[best_m_name] += 1
                    else:
                        top_males_count[best_m_name] = 1
                        
                if best_f_name:
                    if best_f_name in top_females_count:
                        top_females_count[best_f_name] += 1
                    else:
                        top_females_count[best_f_name] = 1

    sorted_males = sorted(top_males_count.items(), key=lambda x: x[1], reverse=True)
    sorted_females = sorted(top_females_count.items(), key=lambda x: x[1], reverse=True)

    print("\nНайпопулярніші чоловічі імена : \n")
    for name, years in sorted_males:
        print(f"{name} {years}")

    print("\nНайпопулярніші жіночі імена : \n")
    for name, years in sorted_females:
        print(f"{name} {years}")

except FileNotFoundError:
    print("Помилка: Файл 'archive.zip' не знайдено.")
except Exception as e:
    print(f"Виникла помилка: {e}")