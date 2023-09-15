'''Напишите программу, которая будет определять самые популярные
имена для детей в выбранном пользователем периоде. Используйте базу
данных из задания 15. Позвольте пользователю выбрать первый и последний
год анализируемого диапазона. В результате программа должна вывести на
экран мужское и женское имена, которые были чаще остальных даны детям в
заданный период времени.
'''
def read_names_file(file_name):
    names_dict = {}
    with open(file_name, 'r') as file:
        for line in file:
            name, count = line.strip().split()
            names_dict[name] = int(count)
    return names_dict
def find_most_popular_names(start_year, end_year, gender):
    most_popular_names = {}
    for year in range(start_year, end_year + 1):
        file_name = f"{year}_{gender}Names.txt"
        names_dict = read_names_file(file_name)
        max_name = max(names_dict, key=names_dict.get)
        most_popular_names[year] = (max_name, names_dict[max_name])

    return most_popular_names
start_year = int(input("Введите начальный год анализируемого диапазона: "))
end_year = int(input("Введите конечный год анализируемого диапазона: "))
gender = input("Введите пол (Boys или Girls): ").capitalize()
most_popular_names = find_most_popular_names(start_year, end_year, gender)
print(f"Самые популярные имена ({gender}) в периоде с {start_year} по {end_year}:")
for year, (name, count) in most_popular_names.items():
    print(f"Год {year}: {name} ({count} раз)")
