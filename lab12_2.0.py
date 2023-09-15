'''Напишите программу, которая будет определять самые популярные
имена для детей в выбранном пользователем периоде. Используйте базу
данных из задания 15. Позвольте пользователю выбрать первый и последний
год анализируемого диапазона. В результате программа должна вывести на
экран мужское и женское имена, которые были чаще остальных даны детям в
заданный период времени.
'''
def read_names_file(file_name):
    names_dict = {}
    with  open(file_name, 'r') as file:
        for line in file:
            name, count = line.strip().split()
            names_dict[name] = int(count)
    return names_dict
def find_most_popular_names(start_year, end_year, gender):
    most_popular_names = {}
    for year in range(start_year, end_year + 1):
        file_name = f"{year}_{gender}Names.txt"
        names_dict = read_names_file(file_name)
        for name, count in names_dict.items():
            if name in most_popular_names:
                if count > most_popular_names[name][1]:
                    most_popular_names[name] = (year, count)
            else:
                most_popular_names[name] = (year, count)
    max_name = max(most_popular_names, key=lambda x: most_popular_names[x][1])
    max_count = most_popular_names[max_name][1]
    most_popular_year = most_popular_names[max_name][0]
    return max_name, max_count, most_popular_year

start_year = int(input("Введите начальный год анализируемого диапазона: "))
end_year = int(input("Введите конечный год анализируемого диапазона: "))
gender = input("Введите пол (Boys или Girls): ").capitalize()
most_popular_name, most_popular_count, most_popular_year = find_most_popular_names(start_year, end_year, gender)
print(f"Самое популярное имя ({gender}) в периоде с {start_year} по {end_year}:")
print(f"{most_popular_name} ({most_popular_count} раз)")
print(f"Самое популярное имя было в {most_popular_year} году.")
