'''Дана строка. Замените в этой строке все появления буквы h на букву H,
кроме первого и последнего вхождения.'''
input_string = input("Введите строку: ")
first_h_index = input_string.find('h')  # Находим индекс первого 'h'
last_h_index = input_string.rfind('h')  # Находим индекс последнего 'h'
if first_h_index != -1 and last_h_index != -1:
    prefix = input_string[:first_h_index + 1]
    middle_part = input_string[first_h_index + 1:last_h_index]
    suffix = input_string[last_h_index:]
    # Заменяем все 'h' в middle_part на 'H'
    middle_part = middle_part.replace('h', 'H')

    new_string = prefix + middle_part + suffix
    print("Результат замены:", new_string)
else:
    print("Буква 'h' не найдена в строке.")
